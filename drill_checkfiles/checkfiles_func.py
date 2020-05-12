import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk




# Importing other modules
import checkfiles_main
import checkfiles_gui


def browseFiles(self):
    global folder_path
    folder_path = StringVar()
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return(filename)




if __name__ == "__main__":
    pass
