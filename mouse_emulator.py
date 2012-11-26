#!/usr/bin/python
import Tkinter as tk
from grid import Grid
from Xlib import X, display
from Xlib.ext.xtest import fake_input

d = display.Display()
screen = d.screen()
screenroot = screen.root

velocity = [0,0]
position = [0,0]
speed = 5

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
    root.after(10,move_pointer)

def press(button):
    fake_input(d, X.ButtonPress, [None, 1, 3, 2, 4, 5][button])

def release(button):
    fake_input(d, X.ButtonRelease, [None, 1, 3, 2, 4, 5][button])

def click(button):
    press(button)
    release(button)

root = tk.Tk()
root.title("Sinch Mouse Emulator")

# Add a tkinter widget
tk.Label(root, text="Select a mouse action").pack()

# Create an accessible button grid
buttons = [ {'text': 'Move Up',      'command': lambda:setvelocity(0,-speed) }
          , {'text': 'Move Down',    'command': lambda:setvelocity(0,speed)  }
          , {'text': 'Move Left',    'command': lambda:setvelocity(-speed,0) }
          , {'text': 'Move Right',   'command': lambda:setvelocity(speed,0)  }
          , {'text': 'Left click',   'command': lambda:click(1)              }
          , {'text': 'Right click',  'command': lambda:click(2)              }
          , {'text': 'Double click', 'command': lambda:click(1)              } # TODO fix
          , {'text': 'Drag',         'command': lambda:press(1)              } ]

controls = Grid(root, 2, 4, buttons)
controls.pack()

root.after(10, move_pointer)
root.mainloop()
