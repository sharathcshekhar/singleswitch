import Tkinter as tk

def split((x, y, a, b)):
    """
    Divides the given square in half and returns the two resulting squares.
    """
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
    def __init__(self, root, rows, cols, buttons):
        self.root = root
        self.rows = rows
        self.cols = cols

        # Set up frame
        tk.Frame.__init__(self, root)

        # Bind keypress handler
        root.bind_all('<Key>', self.keypress)

        # Automatically infer row or column number if omitted
        if rows == None:
            rows = len(buttons) / cols
        elif cols == None:
            cols = len(buttons) / rows

        # Initialize 2d array to hold buttons
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

        # Create buttons
        for r in range(rows):
            for c in range(cols):
                button = tk.Button(self, text="WAT", fg="red")
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

        # Set up selection
        self.divideGrid((0,0,rows,cols))


    def configButtonSquare(self, (x, y, a, b), args):
        """ Configure buttons within the given square """
        for x2 in range(x, a):
            for y2 in range(y, b):
                button = self.buttons[x2][y2]
                button.config(**args)

    def divideGrid(self, selection):
        # Check selection size, if it is 1x1 we are done
        width = abs(selection[0] - selection[2])
        height = abs(selection[1] - selection[3])
        if width == height == 1:
            # TODO: Invoke the button
            # Restore full screen split
            self.divideGrid((0,0,self.rows,self.cols))
            return

        # Split the square
        self.selection1, self.selection2 = split(selection)
        # Color selection 1
        self.configButtonSquare(self.selection1, 
                {'bg': 'red', 'fg': 'black'})
        # Color selection 2
        self.configButtonSquare(self.selection2, 
                {'bg': 'blue', 'fg':'black'})


    def keypress(self, event):
        x = event.char

        if x == "1":
            # Disable selection 2
            self.configButtonSquare(self.selection2, {'bg': 'black'})
            # Split selection 1
            self.divideGrid(self.selection1)

        elif x == "2":
            # Disable selection 1
            self.configButtonSquare(self.selection1, {'bg': 'black'})
            # Split selection 2
            self.divideGrid(self.selection2)

