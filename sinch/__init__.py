from grid import Grid
import Tkinter

def new_window():
    root = Tkinter.Tk(className="sinch")
    root.attributes('-zoomed', '1')

    return root
