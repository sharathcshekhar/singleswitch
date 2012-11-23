import Tkinter as tk

# Demonstration of how to use Tkinter to capture keypress events

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()
    x = event.char
    if x == "w":
        print "W for Wonderful!!!"
    elif x == "a":
        print "A for APPLE!"
    elif x == "d":
        print "D for DANGEROUS!"
    else:
        print "NO ME GUSTA"

root = tk.Tk()
root.bind_all('<Key>', keypress)
root.mainloop()
