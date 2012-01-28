# Welcome To HackJam2.0

This is a Your First Hack (YFH) project. It's a full guide to your first hackathon project - from start to finish. This YFH is to create a web-based Dropbox text editor. When you finish this project, you'll have:

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
2. You'll need the Dropbox Python library. I included it in the Github files to make your life a bit easier, but feel free to install it yourself if you want the satisfaction of doing everything yourself.
3. Check out the example that Dropbox uses, either in the zip that you downloaded from Dropbox, or from the dropbox-examples folder from this Github. Open up web_upload_example.py and put in the two authentication keys Dropbox gave you - the app_key and the app_secret. Run their demo using `python web_upload_example.py` and see what functionality it provides. Now, take a look at the actual file, and try to figure out what Dropbox did to build their application. Parts of this example are actually going to form the first pages of your application, so pay special attention to the login page!

## 4. Learn Mustache (template language)

_Turn hello world into hello, name_


## 5. Make the /login page

_Woot, first serious big steps_

## 6. Make the /viewfiles page

_Damn, your web app actually does something_

## 7. Turn the files into links

_Now it really does something_

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
 - Your website looks like it's from 1990. Learn some more HTML and some CSS - upcoming h@b events. Check out [Twitter Bootstrap](http://twitter.github.com/bootstrap/) for a way to make *beautiful* websites with almost zero work.
 - Add more functionality: rename files, delete files, create files.

