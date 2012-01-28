# pystache2.py
#
# A (currently incomplete implemtation of the mustache2.0 spec in python (https://github.com/mustache/spec)
# Works quite well for the most part, but definitely does not pass all tests in the spec
# 
# Use this library in one of two ways, either with a string or with a file.
#
# import pystache2
# 
# my_web_page1 = pystache2.render_string('Hello {{name}}, {'name':'Kurt'})
# assert my_web_page1 == 'Hello Kurt'
#
# # Contents of myfile.mustache are 'Welcome to Python, {{programmer}}'
# my_web_page2 = pystache2.render_file('myfile.mustache', programmer = 'Cassie')
# assert my_web_page2 == 'Welcome to Python, Cassie'
#
import os
import re
import markupsafe
_escape = markupsafe.escape
_literal = markupsafe.Markup

# VARIABLES
# Feel free to modify these in your code.
CACHING = True
THROW_NOT_FOUND = False
TEMPLATE_DIR = 'views'

# CACHE
_CACHE = {}

# REGEXES
_OTAG = r'\{\{\{?'
_CTAG = r'\}\}\}?'
_TAG = r'[^\}]*'

_ITEMIZER = re.compile('(\r?\n?[ \t]*'+_OTAG+_TAG+_CTAG+'[ \t]*\r?\n?)', re.M) # breaks string into regular strings and {{*}} array
_RE_TAG = re.compile('\\s*(' + _OTAG + '(' + _TAG + ')' + _CTAG + ')\\s*') # recognizes items as tags
_RE_NO_ESCAPE_TAG = re.compile('\s*\{' + _OTAG + _TAG + _CTAG + '\}\\s*')
_ITEM_WHITESPACE = re.compile('(\s*)'+_OTAG+_TAG+_CTAG+'(\s*)')
_ACTION_AND_KEY = re.compile('^([&#\^/>]?) *([a-z\._]+) *$', re.I)

def _render(string, context):
    string = '\n' + string #marker for beginning of string
    item_queue = _ITEMIZER.split(string)
    def closing_index_from_tag_at_index(from_index):
        tag = _RE_TAG.match(item_queue[from_index]).group(2)
        action_and_key = _ACTION_AND_KEY.match(tag)
        key = action_and_key.group(2)

        re_tag_specific_tag = re.compile('\\s*' + _OTAG + '([#\^/])[ \t]*' + key + '[ \t]*'+ _CTAG + '\\s*')
        i = from_index
        indent_level = 0
        while i < len(item_queue):
            match = re_tag_specific_tag.match(item_queue[i])
            if match:
                action = match.group(1)
                if action == '^' or action == '#':
                    indent_level += 1
                elif action == '/':
                    indent_level -= 1
                    if indent_level == 0:
                        return i
            i += 1
        return i

    def leave_white_space(match):
        # take a tag, e.g. a section tag, and leave only the desired whitespace
        whitespace = _ITEM_WHITESPACE.match(match)
        before = re.match('[ \t]*[\r\n]{0,2}', whitespace.group(1)).group(0)
        toss_newline = '\n' in before or '\r' in before
        regex = ('' if toss_newline else '[\r\n]{0,2}') + '[ \t]*$'
        after = re.search(regex, whitespace.group(2)).group(0)

        return before + after

    def context_lookup(key, current_context, context):
        if key == '.':
            return current_context
        keys = key.split('.')
        result = None
        if type(current_context)==dict and keys[0] in current_context:
            result = current_context
        elif type(context)==dict and keys[0] in context:
            result = context
        for k in keys:
            try:
                result = result[k]
            except:
                if THROW_NOT_FOUND:
                    raise ValueError('key not found')
                return None
        return result

    def render_indexes(start_index, end_index, current_context = None, force_no_escape = False):
        result_queue = []
        i = start_index
        while i < end_index:
            match = _RE_TAG.match(item_queue[i])
            if not match: #regular text
                result_queue.append(item_queue[i])
                i += 1
                continue
            tag = match.group(2)
            tag_no_escape = _RE_NO_ESCAPE_TAG.match(item_queue[i])
            if tag.startswith('!'): #commented tag
                result_queue.append(leave_white_space(item_queue[i]))
                i += 1
                continue
            action_and_key = _ACTION_AND_KEY.match(tag)
            action = action_and_key.group(1)
            key = action_and_key.group(2)
            context_value = context_lookup(key, current_context, context)
            if action == '&': #no-escape
                string = re.sub(match.group(1), str(context_value), item_queue[i])
                result_queue.append(string)
                i += 1
                continue
            elif action == '^' or action == '#': #section
                result_queue.append(leave_white_space(item_queue[i]))
                tag = '/ *' + key
                close_index = closing_index_from_tag_at_index(i)
                i += 1
                if action == '^' and not context_value:
                    result_queue.append(render_indexes(i, close_index, context,
                                                       True if tag_no_escape else False))
                elif action == '#' and context_value:
                    if type(context_value) is dict:
                        result_queue.append(render_indexes(i, close_index, context_value,
                                                           True if tag_no_escape else False))
                    elif type(context_value) is list:
                        for subitem in context_value:
                            result_queue.append(render_indexes(i, close_index, subitem,
                                                               True if tag_no_escape else False))
                    elif callable(context_value):
                        lambda_result = context_value(''.join(item_queue[i, close_index]))
                        result_queue.append(str(lambda_result))
                    else:
                        result_queue.append(render_indexes(i, close_index, force_no_escape = 
                                                           True if tag_no_escape else False))
                result_queue.append(leave_white_space(item_queue[close_index]))
                i = close_index + 1
                continue
            elif action == '>': #partial
                result_queue.append(render_file(key, context))
                i += 1
                continue
            elif action == '':
                if tag_no_escape or force_no_escape:
                    string = re.sub(match.group(1), str(context_value), item_queue[i])
                    result_queue.append(string)
                else:
                    string = re.sub(match.group(1), _escape(str(context_value)), item_queue[i])
                    result_queue.append(string)
                i += 1
                continue
            else:
                raise ValueError('Unrecognized tag')

        return ''.join(result_queue)

    result = render_indexes(0, len(item_queue), context)[1:]
    #print str(result).encode('string-escape')
    return result

def render_file(filepath, context=None, **kwargs):
    context = context.copy() if context is not None else {}
    context.update(kwargs)

    filename = os.path.splitext(os.path.basename(filepath))[0]

    string = None
    if CACHING and filename in _CACHE:
        string = _CACHE[filename]
    else:
        found = False
        if not os.path.exists(filepath):
            for (path, dirs, files) in os.walk(TEMPLATE_DIR):
                for fn in files:
                    name = os.path.splitext(fn)[0]
                    if name == filename:
                        filepath = os.path.join(path, fn)
                        found = True
                        break
            if not found:
                raise ValueError('filename %s not found' % (filepath))

        with open(filepath) as f:
            string = f.read()
            if CACHING:
                _CACHE[filename] = string

    return _render(string, context)

def render_string(string, context=None, **kwargs):
    context = context.copy() if context is not None else {}
    context.update(kwargs)
    return _render(string, context)

