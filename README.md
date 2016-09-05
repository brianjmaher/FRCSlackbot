# FRCSlackbot

Dependencies: beautifulsoup4, slackclient
The packages can be installed with PIP by running ~~~~pip install beautifulsoup4~~~~ and ~~~~pip install slackclient~~~~.

To run:
1. Download the repository as a .zip file.
2. Extract the files.
2. Rename "settings_example.py" to "sample.py" and edit the file to contain your Slack API token, the channel you want to post to, the username you want for your bot, the filepath for the event cache, and the desired time between scrapes (in seconds).
3. Open the command prompt.
4. ~~~~cd~~~~ into the FRCSlackbot folder.
5. Run ~~~~python main.py~~~~ 
6. A ~~~~KeyboardInterrupt~~~~ can be used to kill the program. In the command line, this is CTRL + C on Windows/Linux and Command + C on Mac. Alternatively, ~~~~python.exe~~~~ can be terminated via the Task Manager.
