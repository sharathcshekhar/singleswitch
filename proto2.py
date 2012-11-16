#!/usr/bin/python

# simple.py

import wx

# Preferences:
# quick select:
#   Does not allow cancel when you narrow down to one button
#   Instead, automatically selects button
# Highlight speed:
#   Speed it switches row to row / column to column

width = 4
height = 7

app = wx.App()

# The window our app displays in
frame = wx.Frame(None, -1, 'Divide Menu Prototype 1')
# The button grid
gs = wx.GridSizer(width, height, 5, 5)

# Array which holds our buttons
buttons = [[None for x in range(height)] for y in range(width)]

for x in range(0, width):
    for y in range(0, height):
        # Initialize Button
        buttons[x][y] = wx.Button(frame, label='test %s %s' % (x, y))

        # Add button to sizer
        gs.Add(buttons[x][y], 0, wx.EXPAND)


def setColor((x, y, a, b), color):
    """
    Change color of all buttons bounded by the given square.
    """
    # Assert: x < a, y < b
    for x2 in range(x, a):
        for y2 in range(y, b):
            button = buttons[x2][y2]
            button.SetBackgroundColour(color)

def split((x, y, a, b)):
    """
    Divides the given square in half and returns the two resulting squares.
    """
    height = abs(y-b)
    if height != 1:
        # Split in the y direction
        mid = (y+b)/2

        sq1 = (x, y, a, mid)
        sq2 = (x, mid, a, b)
        return (sq1, sq2)

    else:
        # Split in the x direction
        mid = (x+a)/2
        
        sq1 = (x, y, mid, b)
        sq2 = (mid, y, a, b)
        return (sq1, sq2)

def select(s):
    global selection, sq1, sq2
    sq1, sq2 = split(s)
    setColor(sq1, (255,0,0))
    setColor(sq2, (0,255,0))

def reset():
    global selection, sq1, sq2
    selection = (0,0,width,height)
    select(selection)

def keypress(e):
    global selection, sq1, sq2
    key = e.GetKeyCode()
    if chr(key) == 'R':
        # Disable sq2
        setColor(sq2, (0,0,0))
        # Set new selection
        selection = sq1
        select(selection)
    elif chr(key) == 'G':
        # Disable sq2
        setColor(sq1, (0,0,0))
        # Set new selection
        selection = sq2
        select(selection)

    width = abs(selection[0] - selection[2])
    height = abs(selection[1] - selection[3])
    if width == height == 1:
        reset()

reset()

# Add event handler
buttons[0][0].Bind(wx.EVT_KEY_DOWN, keypress)

# Display everything
frame.SetSizer(gs)
frame.Show()
app.MainLoop()

