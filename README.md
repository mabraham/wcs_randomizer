# Installation

1. Open a command terminal

2. Install python >= 3.7

3. Clone from github e.g.

```
git clone https://github.com/mabraham/wcs_randomizer.git
```

4. Change the working directory to that e.g.

```
cd wcs_randomizer
```

5. Get python dependencies (only the simple web server Django, which will just run locally on your laptop)

```
python3 -m pip install -r requirements.txt
```

or if that somehow fails because python3 isn't found, try

```
python -m pip install -r requirements.txt
```

6. Ensure you are will be using the Chrome browser.
Back when I wrote this, only Chrome would work.
Maybe Safari supports this now, but you're on your own there.

# Running

1. Configure the local Django web server like

```
python3 manage.py migrate
python3 manage.py createsuperuser
```

Use any name and password you find memorable, but don't use a password whose secrecy you actually care about!
You don't need to give it a real email address.
Ignore any warnings.

2. Now the server is configured. You can now run the web server like

```
python3 manage.py runserver
```

This terminal needs to keep runinng in order to keep the server running.
If you want to stop the server, kill the terminal, or press Ctrl-C.

You will see a bunch of stuff including something like

```
Starting development server at http://127.0.0.1:8000/
```

That link tells Chrome to ask the local web server we just ran for content.
Your link might be different.
That's fine, use the one you see.
If you just go to it, then you'll get a page showing an error that there's no content (404).
That's because I was lazy and didn't build something that I didn't need.
However, there are three subpages that are relevant, respectively `randomizer/admin`, `randomizer/spotlight`, and `randomizer/spotlight_mc`.
You will need to open and use all three - read on!

3. Open the admin page in Chrome at URL like http://127.0.0.1:8000/randomizer/admin

Make a bookmark so you can find it again easily.

Eventually you'll get to an admin page where you will see a heading "RANDOMIZER" with a sub-heading "Spotlight dancers."
This is where you get to enter the names of the dancers who will be drawn out, along with their bib number.
You can do all this whenever the finalists are known, and then not touch it again.
You need to enter all the dancers from the role with the fewest dancers here.
So if there are 5 leaders and 7 followers, leaders names will be drawn out by followers.
The dancers from the other role are irrelevant and not entered at all.
Ignore stuff about users and groups - you'd only want that for running some kind of real web server, and we're just abusing Django to let one Chrome tab control what appears on another.

Click on `+Add`, then enter a bib number and a full name for a dancer.
Don't click on the "Has danced" box - that will get filled in by the system as the dancers dance.
You could change that manually if you like making problems - just don't.
Press "Save and add another" or "SAVE" as appropriate, until you've entered all the dancers.
Go ahead and fill in some dancers to experiment with.

Review all the names and bib numbers.
If names use non-English characters that will probably work fine, but do test!

4. Now go to the display page at URL like http://127.0.0.1:8000/randomizer/spotlight

Make a bookmark so you can find it again easily.
This tab should go in its own browser window that you are prepared to put on its own desktop, so you can just change desktops to go from Flapper display to the background for other times.
Check it looks ok.
You can't do anything on this webpage, it's just the display.

5. Now go to the MC page at URL like http://127.0.0.1:8000/randomizer/spotlight_mc

Make a bookmark so you can find it again easily.
Here's where things are controlled during the spotlights.

"Clear spotlight display" removes any currently displayed dancer and bib number.
If there's none shown, it does nothing.
You can't undo this, so don't click it randomly!
It's a good idea to use this to clear the names after the judges have seen the bib number, around when the music starts.
Or use it after the desktop has switched to whatever display should appear while the dancers are dancing.

"Choose random dancer" is used when the MC wants a partner drawn.
Internally, that sets the "Has danced" flag, which ensures this name will not be drawn again.

"Let all dancers dance again" is the exception to this.
It clears the "Has danced" flag from all dancers and now any name can be drawn again.

For example, if there are 5 leaders to draw for 7 followers, we want to "Choose random dancer" five times.
The fifth one will be known to everyone after the fourth is drawn, of course.
After the fifth one, choose "Let all dancers dance again" and now the sixth "Choose random dancer" will be random from all five leaders.
Finally the last "Choose random dancer" chooses from among the remaining four leaders who already danced one time.

You want to have this tab open on a desktop that you aren't going to show.

# How-tos

## Clean up

After you are done experimenting, exit the server (e.g. Ctrl-C on its terminal window).
There is now a file `db.sqlite3` which has the admin user and password along with the information you entered on the admin page.
If you would now restart the server, all the same dancers are preserved, along with whether they have danced.
Thus, no disaster if you accidentally exit the server on the night.
The same URLs will continue working once you start a new server.
(Don't start a second server, however, that will use a different port like 8001 or something.)

To clean up, simply delete that file.
Then you must reconfigure the webserver (migrate and createsuperuser above) and enter new dancers.

## If something goes wrong

Switch to manual drawing!
