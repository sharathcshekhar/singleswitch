#!/usr/bin/python
import Tkinter as tk
from grid import Grid
from Xlib import X, display

d = display.Display()
screenroot = d.screen().root

velocity = [5,0]
position = [0,0]

def setvelocity(u, d):
    global velocity
    velocity = [u,d]

def move_pointer():
    position[0] += velocity[0]
    position[1] += velocity[1]
    screenroot.warp_pointer(position[0],position[1])
    d.sync()
    root.after(90,move_pointer)

root = tk.Tk()
root.title("Sinch Mouse Emulator")

# Add a tkinter widget
tk.Label(root, text="Select a mouse action").pack()

# Create an accessible button grid
buttons = [ {'text': 'Move Up', 'command': lambda:setvelocity(0,-5)}
          , {'text': 'Move Down', 'command': lambda:setvelocity(0,5)}
          , {'text': 'Move Left', 'command': lambda:setvelocity(-5,0)}
          , {'text': 'Move Right', 'command': lambda:setvelocity(5,0)}
          , {'text': 'Left click'}
          , {'text': 'Right click'}
          , {'text': 'Double click'}
          , {'text': 'Drag'} ]

Grid(root, 2, 4, buttons).pack()

root.after(90, move_pointer)
root.mainloop()
