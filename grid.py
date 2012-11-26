"""
Grid Module

Part of the Sinch package.
Provides a single-switch accessible grid widget for Tkinter.
"""

import Tkinter as tk

class Grid(tk.Frame):
    """ Single-Switch Accessible Button Grid Widget """

    def __init__(self, root, rows, cols, configs):
        # Set up frame
        tk.Frame.__init__(self, root)

        # Bind keypress handler
        root.bind_all('<Key>', self.keypress)

        # Automatically infer row or column number if omitted
        if rows == None:
            rows = len(configs) / cols
        elif cols == None:
            cols = len(configs) / rows

        # Instance variables
        self.root = root
        self.rows = rows
        self.cols = cols

        # Initialize 2d array to hold buttons
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

        # Create buttons
        for r in range(rows):
            for c in range(cols):
                index = (r*cols)+c
                button = tk.Button(self, **configs[index])
                button.grid(row=r, column=c, sticky='nsew')
                self.buttons[r][c] = button

        # Create manager
        self.manager = DivideManager(self)

    def configure_buttons(self, (x, y, a, b), args):
        """Configure all the buttons within the given rectangular region of the grid"""

        for i in range(x, a):
            for j in range(y, b):
                button = self.buttons[i][j]
                button.config(**args)

    def keypress(self, event):
        """Key event handler. Acts as a placeholder until we get code to
        handle actual single switch devices. """

        x = event.char

        if x == "b":
            self.manager.typeb()

        elif x == "a":
            self.manager.typea()

class GridManager(object):
    """ Defines the behavior of the grid. """

    def __init__(self, grid):
        raise NotImplementedError

    def typea(self):
        raise NotImplementedError

    def typeb(self):
        raise NotImplementedError

def split((x, y, a, b)):
    """Divides the given square in half and returns the two resulting
    squares."""

    width = abs(x-a)
    height = abs(y-b)
    if width >= height:
        # Split in the x direction
        mid = (x+a)/2
        
        sq1 = (x, y, mid, b)
        sq2 = (mid, y, a, b)
        return (sq1, sq2)
    else:
        # Split in the y direction
        mid = (y+b)/2

        sq1 = (x, y, a, mid)
        sq2 = (x, mid, a, b)
        return (sq1, sq2)

class DivideManager(GridManager):
    """ Divide and conquer style grid selection """

    def __init__(self, grid):
        self.grid = grid
        self.rows = self.grid.rows
        self.cols = self.grid.cols

        # Set up selection
        self.divide_grid((0, 0, self.rows, self.cols))


    def divide_grid(self, selection):
        """Select a rectangular region of the grid"""

        # Check selection size, if it is 1x1 we are done
        width = abs(selection[0] - selection[2])
        height = abs(selection[1] - selection[3])
        if width == height == 1:
            # TODO: Invoke the button
            self.grid.buttons[selection[0]][selection[1]].invoke()
            # Restore full screen split
            self.divide_grid((0,0,self.rows,self.cols))
            return

        # Split the square
        self.selection1, self.selection2 = split(selection)
        # Color selection 1
        self.grid.configure_buttons(self.selection1, 
                {'bg': 'red', 'fg': 'black'})
        # Color selection 2
        self.grid.configure_buttons(self.selection2, 
                {'bg': 'blue', 'fg':'black'})

    def typea(self):
        # Disable selection 2
        self.grid.configure_buttons(self.selection2, {'bg': 'black'})
        # Split selection 1
        self.divide_grid(self.selection1)

    def typeb(self):
        # Disable selection 1
        self.grid.configure_buttons(self.selection1, {'bg': 'black'})
        # Split selection 2
        self.divide_grid(self.selection2)
