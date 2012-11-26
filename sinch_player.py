#!/usr/bin/python
import Tkinter as tk
import mpd
import sys
from pprint import pprint
from random import choice
from socket import error as SocketError
from sinch import Grid

# Settings
HOST = 'localhost'
PORT = '6600'

volume = 100
client = mpd.MPDClient()
try:
    client.connect(host=HOST, port=PORT)
except SocketError:
    print "Failed to connect to MPD. Are you sure it's installed and running on port %s?" % PORT
    sys.exit(1)

# Don't shuffle randomly (better for demo if we don't)
client.random(0)
# Repeat the playlist
client.repeat(1)

pprint(client.status())
pprint(client.stats())
#pprint(client.idle('player'))

# Check database for any updates
client.update()
# Clear current playlist
client.clear()
# Add entire database to playlist
client.add("/")

pprint(client.playlistinfo())

def play():
    status = client.status()
    if (status["state"] == "play"):
        client.pause()
    else:
        client.play()

root = tk.Tk()

tk.Label(root, text="A label, outside the grid").pack()

# Create an accessible button grid
buttons = [ {'text': 'Play',           'command': play }
          , {'text': 'Next',           'command': client.next }
          , {'text': 'Previous',       'command': client.previous }
          , {'text': 'Stop',           'command': client.stop }
          , {'text': 'Volume Up',      'command': client.play }
          , {'text': 'Volume Down',    'command': client.play } ]

Grid(root, 2, 3, buttons).pack()

# Closing the window also closes connection to mpd
def close():
    client.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# Start gui loop
root.mainloop()
