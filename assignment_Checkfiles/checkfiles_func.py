import os
import shutil
import datetime
from tkinter import *
from tkinter import filedialog
import tkinter as tk




# Importing other modules
import checkfiles_main
import checkfiles_gui

def close_window(self):
    self.master.destroy()
    os._exit(0)

def browseFiles(self):
    global source
    source = filedialog.askdirectory() + "/"
    self.txt_browse1.insert(0,source)

def browseFiles2(self):
    global dest
    dest = filedialog.askdirectory() + "/"
    self.txt_browse2.insert(0,dest) 


def checkFiles(self):
    files = os.listdir(source) 
    for i in files:
        if datetime.datetime.now().timestamp() - os.path.getmtime(source) < 64800:
            shutil.move(source+i, dest)    
    

            
    
        


        
        




if __name__ == "__main__":
    pass
