#!/usr/bin/python
import Tkinter as tk
import sinch
import os

root = sinch.new_window()

# Add a tkinter widget
tk.Label(root, text="A label, outside the grid").pack(expand=1, fill='both')

def run(script):
    os.system(script)

# Create an accessible button grid
buttons = [ {'text': 'Sinch Player',   'command':lambda:run('./sinch_player.py &') }
          , {'text': 'Mouse Emulator', 'command':lambda:run('./mouse_emulator.py &') } ]

sinch.Grid(root, 1, 2, buttons).pack(expand=1, fill='both')

# You can still add other widgets
tk.Label(root, text="Another external label").pack(expand=1, fill='both')

root.mainloop()
