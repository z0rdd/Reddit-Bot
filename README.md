# Reddit-Bot
This is a simple webapp gathering data from reddit and displaying some simple stats and visualizations.
The app has 2 operation modes one for localhost and one for Heroku, and it automatically chooses the appropriate one.
The module gathering data from reddit utilizes PRAW and is an independent scheduled task running in the background.
The web module is running on Flask and both modules are connected to the same PostgreSQL database.
