#!/usr/bin/python
import Tkinter as tk
from grid import Grid

root = tk.Tk()

# Add a tkinter widget
tk.Label(root, text="A label, outside the grid").pack()

# Create an accessible button grid
buttons = [ {'text': 'Play'}
          , {'text': 'Skip Forward'}
          , {'text': 'Skip Backwards'}
          , {'text': 'Stop'}
          , {'text': 'Volume Up'}
          , {'text': 'Volume Down'} ]

Grid(root, 2, 3, buttons).pack()

# You can still add other widgets
tk.Label(root, text="Another external label").pack()

root.mainloop()
