import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk




# Importing other modules
import checkfiles_main
import checkfiles_gui


def browseFiles(self):
    filename = filedialog.askdirectory()
    self.txt_browse1.insert(0,filename)
    




if __name__ == "__main__":
    pass
