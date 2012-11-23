import Tkinter as tk

class Grid(tk.Frame):
    def __init__(self, root, rows, cols, buttons):
        self.root = root

        # Set up frame
        tk.Frame.__init__(self, root)

        # Bind keypress handler
        root.bind_all('<Key>', self.keypress)

        # Automatically infer row or column number if omitted
        if rows == None:
            rows = len(buttons) / cols
        elif cols == None:
            cols = len(buttons) / rows

        for r in range(rows):
            for c in range(cols):
                tk.Button(self, text="WAT", fg="red").grid(row=r, column=c)
                

    def keypress(self, event):
        if event.keysym == 'Escape':
            self.root.destroy()

        x = event.char
        if x == "w":
            print "W for Wonderful!!!"
        elif x == "a":
            print "A for APPLE!"
        elif x == "d":
            print "D for DANGEROUS!"
        else:
            print "NOOOOO"
