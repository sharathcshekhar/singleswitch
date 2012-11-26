#!/usr/bin/python
import Tkinter as tk
from grid import Grid
from Xlib import X, display

d = display.Display()
screen = d.screen()
screenroot = screen.root

velocity = [0,0]
position = [0,0]

def setvelocity(u, d):
    global velocity
    velocity = [u,d]

def bound(num, m):
    if num < 0: return 0
    elif num > m: return m
    else: return num

def move_pointer():
    position[0] = bound(position[0] + velocity[0], screen.width_in_pixels)
    position[1] = bound(position[1] + velocity[1], screen.height_in_pixels)
    screenroot.warp_pointer(position[0],position[1])
    d.sync()
    root.after(90,move_pointer)

root = tk.Tk()
root.title("Sinch Mouse Emulator")

# Add a tkinter widget
tk.Label(root, text="Select a mouse action").pack()

# Create an accessible button grid
buttons = [ {'text': 'Move Up', 'command': lambda:setvelocity(0,-10)}
          , {'text': 'Move Down', 'command': lambda:setvelocity(0,10)}
          , {'text': 'Move Left', 'command': lambda:setvelocity(-10,0)}
          , {'text': 'Move Right', 'command': lambda:setvelocity(10,0)}
          , {'text': 'Left click'}
          , {'text': 'Right click'}
          , {'text': 'Double click'}
          , {'text': 'Drag'} ]

controls = Grid(root, 2, 4, buttons)
controls.pack()

root.after(90, move_pointer)
root.mainloop()
