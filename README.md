# Welcome To HackJam2.0

This is a Your First Hack (YFH) project. It's a full proposal for what to do during your first hackathon - from start to finish. You'll build your very first web application. And not a dumb one either, but a web application that has some seriously awesome functionality, and you could absolutely use day-to-day. This YFH is to create a web-based Dropbox text editor. When you finish this project, you'll have:

* learned about OAuth, a way for you to securely use other applications (like Dropbox) without having your users give away their username and password.
* connected your application with the Dropbox API, allowing your application to act exactly like any application that Dropbox creates themselves.
* created a fully functional web application that other people can use by visiting it's URL.
* learned a ton of Python and HTML.
* learned how to use several 3rd party libraries to make your job easier and your project more robust.
* kicked some serious ass!

Now, let's get started!

## 0. Before You Start (Read This!)

First of all, the most important thing you should take away from this tutorial: don't be afraid to ask. Or be afraid and do it anyway, whichever works for you. Take away that message and you're done reading. That's it, you're done, go have fun hacking! If you're still reading, here's the idea: development is fundamentally about problem solving. And problems are difficult - otherwise they wouldn't be problems. With all the problems that constantly crop up when you're programming, the only hope you have to tackle all the challenges is to ask for assistance from time to time. When your Python program isn't working, ask the person next to you if s/he has any experience with pdb, the Python debugger. When your database just won't do what you tell it to do, walk up to that group of people chatting by the boxes of pizza and ask if any of them know some SQL-fu. And keep asking till you get the answers you're looking for. Don't be afraid to post your questions to Stack Overflow. And finally, share what you learn. Somebody else probably isn't as brave as you and didn't ask the questions they had. So, tell the person next to you when you learn how to write your first Hello World web application using the Bottle framework in Python. Face it, that's freakin' awesome, and the person next to you is going to learn about something they didn't even know was cool.

Now that you're pumped up to get started, here are some quick tips for when you hit your first roadblocks.

 - Ask other people around the room, or the group of people already chatting, or anyone else. What I said before, not kidding!
 - Ask Google. It has the right answers a lot of the time.
 - If you've asked several people and are getting stuck, consider asking one of these awesome people for help:
 <table><tr><td><img src="http://a4.sphotos.ak.fbcdn.net/hphotos-ak-ash4/404538_10150513294741510_659756509_9200351_1366359412_n.jpg" width="200" height="auto"></td>
 <td><img src="http://a2.sphotos.ak.fbcdn.net/hphotos-ak-snc7/305492_10150364954364573_516544572_7885545_1515202994_n.jpg" width="200" height="auto"></td>
 <td><img src="http://a7.sphotos.ak.fbcdn.net/hphotos-ak-snc7/384004_2411869338209_1295520723_32474578_382624553_n.jpg" width="200" height="auto"></td>
 <td><img src="http://a3.sphotos.ak.fbcdn.net/hphotos-ak-snc7/378155_2381360535508_1295520723_32462104_1169991459_n.jpg" width="200" height="auto"></td>
 </tr><tr><td>Kurt Spindler</td><td>Nelson Zhang</td><td>Michelle Bu</td><td>Eric Zhang</td></tr></table>

You'll need to install Python. If you've never used Python before and you've had something missing in your life, Python is probably the answer. If so, go download and install Python. That's step 1 for the project. Go!

## 1. Learn Python

Hopefully, you remember some of your Python from 61A. If you've forgotten a bit, head over to the [official Python tutorial](http://docs.python.org/tutorial/) (It's amazing!), and refresh your memory.

## 2. Learn Bottle (web server)

Bottle.py is a library for Python to make websites _extremely_ quickly. Install it, and then write a Hello World from the [Bottle tutorial](http://bottlepy.org/docs/dev/tutorial.html).

## 3. Add Dropbox authentication

Dropbox is a wonderful company for any number of reasons - not least of which because they provide you with a fantastic Python library to use their services. Check it out at [their site](https://www.dropbox.com/developers). That being said, there's a lot of stuff on that site, so here are a few hotspots to check out.

1. Dropbox keeps a record of your app to ensure security. You'll first need to create an app with Dropbox in order to use their services. Go [here](https://www.dropbox.com/developers/apps) to create your app on Dropbox.
2. You'll need the Dropbox Python library. I included it in the Github files to make your life a bit easier, but feel free to install it yourself using pip or from Dropbox's website if you want the satisfaction of doing everything yourself.
3. Check out the example that Dropbox uses, either in the zip that you downloaded from Dropbox, or from the dropbox-examples folder from this Github. Open up web_upload_example.py and put in the two authentication keys Dropbox gave you - the app_key and the app_secret. Run their demo using `python web_upload_example.py` and see what functionality it provides. Now, take a look at the actual file, and try to figure out what Dropbox did to build their application. Parts of this example are actually going to form the first pages of your application, so pay special attention to the login page!

## 4. Start Building Your Web App!

Alright, so here's where we get down and dirty and actually start to build your web app. You're gonna have to start writing some of your own code here. Also, it's gonna start becoming a bit more free form, so feel free to try things that might not work, make mistakes, and generally be willing to try things until they work. You're discovering how to build stuff, so expect that you'll get a bit frustrated sometimes, but just keep on going, because the end result is gonna be awesome. Don't give up!

Start with a new version of the bottle.py Hello World application. Just to make discussion easier, call this file `app.py`. Modify it to be a web page with a single link, at first just to Dropbox's homepage. Make sure this web page works fine by running the Bottle server and visiting the web page. Now, just add one thing before continuing. Add an `import dropbox` line at the top of `app.py`, and make sure it still works. You'll need the Dropbox library installed for this to work. 

Once you've done that, start looking at how Dropbox's example website does the authentication on it's `/login` page. You're going to need to add all the same features to your bottle application. A few hints: The host is the base of the URL you're on. For the URL `http://www.dropbox.com/myfile`, the host is `www.dropbox.com`. Notice for most of your bottle development, your host has probably been `localhost:8080` (or maybe some other port). The dropbox example finds the name of the host using `self.host`. In bottle, you'll use `bottle.request.headers['host']`. I'd also copy the `get_session()` and `get_client()` functions into your python file. It will make your life a bit easier.

For reference, here is the Dropbox login page.

    sess = get_session()
    request_token = sess.obtain_request_token()
    TOKEN_STORE[request_token.key] = request_token
    
    callback = "http://%s/callback" % (self.host)
    url = sess.build_authorize_url(request_token, oauth_callback=callback)
    prompt = """Click <a href="%s">here</a> to link with Dropbox."""
    return prompt % url 

The reason this page is a bit complicated is because it holds the OAuth (the way Dropbox verifies users) logic for the application. It first creates a key for the user's session, this user's single visit, or session, to your website. Your website then asks Dropbox to verify that user for the duration of their session, and asks you to provide a callback URL that the Dropbox website will bring your user to once they've finished logging in to Dropbox.

You're going to want all this same logic: storing their session token, providing a callback URL, and building the string that creates the webpage for your bottle application. You should also construct a new route and function for `/callback`, which is the URL you want Dropbox to return you to. This page should also include the same logic as `callback_page()` in the Dropbox example. Try to make it work!

## 4. Status Check

Awesome job. So, just a status check, you should now have a basic website, consisting of two pages. The first should present a login link to the user. When that pages loads, it should be doing all the same OAuth work in the background that the Dropbox example does. After the user clicks on that link and goes to Dropbox, Dropbox should redirect the user to a new webpage, call it `/callback`, which should store the data returned from Dropbox, just like the Dropbox example does. Feel free to print out some data on the page for verification. 

If you've made it this far, take a minute to give yourself a huge pat on the back. You've mastered OAuth, creating a web server, using 3rd party libraries, and integrated with Dropbox. Damn good job.

## 5. Make the /viewfiles page

Alright, so now we want to do something with the Dropbox integration. Let's make a simple view of all our files. To do this, you should use a templating engine called [mustache](mustache.github.com). It's incredibly powerful, and beautiful as well. Everything is expressed with variable names surrounded by mustaches. {{like this}}. Read about that until you're a little comfortable with it. Then add this line to the top of `app.py`: `import pystache2`. The pystache2.py file is available at this project's Github page. Create a new route in your bottle file to test out using the templates, and get yourself a little comfortable with it. There's documentation on pystache2 within the `pystache2.py` file.

Now, let's make the `/viewfiles` page. Create this route and function in bottle.

First, we're going to need some data to populate the page with. Within the function for this page, we're going to need to query the Dropbox servers for the list of files in a directory. Check out the following code I wrote.

    access_token_key = bottle.request.get_cookie('access_token_key') #gets the access_token_key from the user's cookies
    access_token = TOKEN_STORE[access_token_key] #gets the actual access_token from the server's cache `TOKEN_STORE` based on the key on the previous line
    client = get_client(access_token) #get_client, the function from the Dropbox example code
    context = client.metadata('.') #client.metadata is the Dropbox library call to get the list of files in the directory. You should look at the documentation of the Dropbox Python library to confirm this.

For now, just have this webpage return `str(context)` and confirm that you're getting the data correctly. If you are, congradulations. Get another big pat on the back, and keep going!

You need to present this data in a more readable fashion - this is where the templates come in. Make a template `viewfiles.mustache`. It should have a mustache section (remember, in mustache, a section is a group that gets repeated or otherwise treated in a special way.) that will display something for every file within a directory. My version displays the name and the date modified, and wraps it within a HTML table. You should look at the keys of the context dictionary to figure out the names of variables you can use in your template.

Once that template is up and running, change your function to have `return pystache2.render_file('viewfiles', context)` instead of just printing the dictionary. Once you get this figured out, this starts looking like a real web app. Awesome!

## 7. Turn the files into links

Now, you need to be able to go deeper into Dropbox folders instead of just looking at the root folder. You should add a \<:path\> to the end of the viewfiles route so that it reads

    @bottle.route('/viewfiles/<path:path>')
    def viewfiles(path = '.'):
        ...

Now, you have a variable named path available within this function, which reprenents your current location in Dropbox. Change the function to use this path instead of the generic one, and you're one step closer! Sweet!

_Change Things IntoFiles_


## 8. Make the file page

_Now you can view files, damn!_

## 9. Turn that into a text editor

_Holy crap_

## 10. Add the save button

_On a roll_

## 11. The really hard part

_Celebrate! You're done! Tell your neighbors. Get in line to present. Freakin awesome_

## 11. Where next?

_Brainstorm what else you could do with this project, or what other things you could build_
Few ideas:

- Your website looks like it's from 1990. Learn some more HTML and some CSS (there are some upcoming H@B events to teach this stuff!). Check out [Twitter Bootstrap](http://twitter.github.com/bootstrap/) for a way to make *beautiful* websites with almost zero work.
- Add more functionality: rename files, delete files, create files.

