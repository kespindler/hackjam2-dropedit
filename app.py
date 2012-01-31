#!/usr/bin/env python
import bottle
import pystache2
import dropbox
import webtools

CFG = webtools.ServerConfig()

bottle.debug(CFG.IS_DEV)

route = bottle.route

APP_KEY = CFG.get('dropbox', 'app_key')
APP_SECRET = CFG.get('dropbox', 'app_secret')
ACCESS_TYPE = CFG.get('dropbox', 'access_type')

HOST = None # override this if the server complains about missing Host headers
TOKEN_STORE = {}

def get_session():
    return dropbox.session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

def get_client(access_token):
    sess = get_session()
    sess.set_token(access_token.key, access_token.secret)
    return dropbox.client.DropboxClient(sess)

@route('/')
def index():
    sess = get_session()
    request_token = sess.obtain_request_token()
    TOKEN_STORE[request_token.key] = request_token
    host = bottle.request.headers['host']
    callback = "http://%s/callback" % (host)
    url = sess.build_authorize_url(request_token, oauth_callback=callback)
    prompt = """Click <a href="%s">here</a> to link with Dropbox.""" % url
    return prompt

@route('/callback')
def callback():
    sess = get_session()
    oauth_token = bottle.request.params.oauth_token
    request_token = TOKEN_STORE[oauth_token]
    access_token = sess.obtain_access_token(request_token)
    TOKEN_STORE[access_token.key] = access_token
    bottle.response.set_cookie('access_token_key', access_token.key)
    return bottle.redirect('/viewpath/')

@route('/viewpath/<path:path>')
def viewfiles(path = '.'):
    access_token_key = bottle.request.get_cookie('access_token_key')
    access_token = TOKEN_STORE[access_token_key]
    client = get_client(access_token)
    context = client.metadata(path)
    if context['is_dir']:
        host = bottle.request.headers['host']
        page_name = 'http://' + host + '/viewpath'
        return pystache2.render_file('viewfiles', context, page_name = page_name)
    else:
        print context
        fileobject = client.get_file(path)
        filedata = fileobject.fp.read(fileobject.length)
        rev_version = context['rev']
        return pystache2.render_file('editfile', filedata = filedata, filename = path, filerevversion = rev_version)

@route('/submitfileupdate', method='POST')
def submitfileupdate():
    filedata = bottle.request.params.filearea
    filepath = bottle.request.params.filepath
    filerevversion = bottle.request.params.filerevversion
    filedata.replace('\r\n', '\n')
    access_token_key = bottle.request.get_cookie('access_token_key')
    access_token = TOKEN_STORE[access_token_key]
    client = get_client(access_token)
    result = client.put_file(filepath, filedata, parent_rev = filerevversion)
    return 'Update complete!\r\nmetadata: %s' % str(result)

@route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='./static')

bottle.run(host='localhost', port = CFG.PORT, reloader = CFG.IS_DEV)

