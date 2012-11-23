"""
Grid Module

Part of the Sinch package.
Provides a single-switch accessible grid widget for Tkinter.
"""

import Tkinter as tk

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
                print index
                button = tk.Button(self, **configs[index])
                button.grid(row=r, column=c, sticky='nsew')
                self.buttons[r][c] = button

        # Set up selection
        self.divide_grid((0, 0, rows, cols))

    def configure_buttons(self, (x, y, a, b), args):
        """Configure all the buttons within the given region"""

        for i in range(x, a):
            for j in range(y, b):
                button = self.buttons[i][j]
                button.config(**args)

    def divide_grid(self, selection):
        """Select a rectangular region of the grid"""

        # Check selection size, if it is 1x1 we are done
        width = abs(selection[0] - selection[2])
        height = abs(selection[1] - selection[3])
        if width == height == 1:
            # TODO: Invoke the button
            # Restore full screen split
            self.divide_grid((0,0,self.rows,self.cols))
            return

        # Split the square
        self.selection1, self.selection2 = split(selection)
        # Color selection 1
        self.configure_buttons(self.selection1, 
                {'bg': 'red', 'fg': 'black'})
        # Color selection 2
        self.configure_buttons(self.selection2, 
                {'bg': 'blue', 'fg':'black'})

    def keypress(self, event):
        """Key event handler. Acts as a placeholder until we get code to
        handle actual single switch devices. """

        x = event.char

        if x == "1":
            # Disable selection 2
            self.configure_buttons(self.selection2, {'bg': 'black'})
            # Split selection 1
            self.divide_grid(self.selection1)

        elif x == "2":
            # Disable selection 1
            self.configure_buttons(self.selection1, {'bg': 'black'})
            # Split selection 2
            self.divide_grid(self.selection2)

