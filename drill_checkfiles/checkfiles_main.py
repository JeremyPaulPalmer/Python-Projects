# Python Ver:   3.8.2
#
# Author:       Jeremy Palmer
#
# Purpose:      Check files GUI Drill; Python Course
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Importing gui
import checkfiles_gui


# Tkinter frame we are inheriting from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Frame configuration
        self.master = master
        self.master.minsize(750,275)
        self.master.maxsize(750,275)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
                

        # Load gui from separate file
        checkfiles_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
