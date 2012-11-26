#!/usr/bin/python
import Tkinter as tk
import mpd
import sys
from socket import error as SocketError
from grid import Grid

# Settings
HOST = 'localhost'
PORT = '6600'

client = mpd.MPDClient()

try:
    client.connect(host=HOST, port=PORT)
except SocketError:
    print "Failed to connect to MPD. Are you sure it's installed and running on port %s?" % PORT
    sys.exit(1)

client.update()

print client.status()
print client.stats()

def play():
    status = client.status()
    if (status["state"] == "play"):
        client.pause()
    else:
        client.play()

root = tk.Tk()

# Create an accessible button grid
buttons = [ {'text': 'Play',           'command': play }
          , {'text': 'Next',           'command': client.next }
          , {'text': 'Previous',       'command': client.previous }
          , {'text': 'Stop',           'command': client.stop }
          , {'text': 'Volume Up',      'command': client.play }
          , {'text': 'Volume Down',    'command': client.play } ]

Grid(root, 2, 3, buttons).pack()

root.mainloop()
