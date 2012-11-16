#!/usr/bin/python

# Look into xpyb, python bindings to xcb?
from Xlib import X, display
d = display.Display()
s = d.screen()
root = s.root
root.warp_pointer(100,100)
d.sync()
