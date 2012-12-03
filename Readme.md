Dependencies
-------------
* python
* python-tk
* python-mpd
* python-xlib
* wmctrl

Ubuntu Quick Start
-------------------
* sudo apt-get install python python-tk python-mpd python-xlib wmctrl
* sudo vim /etc/mpd.conf
    * Change music_directory to wherever you keep your music
* sudo service mpd restart

Running the Program
--------------------
Simply execute:
    python launcher.py

The launcher allows you to run Sinch applications, specifically the Sinch music player and the Sinch mouse emulator. You can also launch these appications directly by running:
    python sinch_player.py
    python mouse_emulator.py

To navigate the applications, press 'r' to select the red region, or 'b' to select the blue region.
