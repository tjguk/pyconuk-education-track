* Call create.cmd

  This deletes the database file if it's there and the creates it directly
  from SQL (ie without using Python) with no data. It will then call
  create-bookings.py which uses sqlite3 to rebuild the data.

* Run run.cmd

  This runs the website.py, which uses the single-module bottle.py framework
  in the same directory and then starts the webbrowser at the right address.

Alternatively:

* Run wsgiapp.py which uses Python-only tools to build the website. More work
  (you'll have to re-implement the things which bottle.py does for you) but
  works without any extra downloads

Files of notes: (none exhaustive)

* help-resources.txt -- places to go for help with Python

* web-hosts.txt -- where you might host Python webserver code

* websites.txt -- different Python tools to help build websites

* orms.txt -- examples of popular ORMs.

