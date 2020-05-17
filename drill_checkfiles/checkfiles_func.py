import os
import fnmatch
import shutil
import datetime
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3




# Importing other modules
import checkfiles_main
import checkfiles_gui

def close_window(self):
    self.master.destroy()
    os._exit(0)

def browseFiles(self):
    global filename
    filename = filedialog.askdirectory()
    self.txt_browse1.insert(0,filename)

def browseFiles2(self):
    global filename2
    filename2 = filedialog.askdirectory()
    self.txt_browse2.insert(0,filename2)


def checkFiles(self):
    folder_list = os.listdir(filename)
    desired = '*.txt'
    matchingText = fnmatch.filter(folder_list, desired)
    for i in matchingText:
        oldPath = os.path.join(filename, i)
        newPath = os.path.join(filename2, i)
        conn = sqlite3.connect('movedFiles.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_files TEXT, \
                col_mtime TEXT \
                )")
            cur.execute("INSERT INTO tbl_files(col_files) VALUES (?)", \
                        (str.split(i)))
            conn.commit()
        conn.close()
        shutil.move(oldPath, filename2)
        print(newPath + ' ' + str(datetime.datetime.fromtimestamp(os.path.getmtime(newPath))))
    modStamp = str(datetime.datetime.fromtimestamp(os.path.getmtime(newPath)))
    for i in modStamp:
        conn = sqlite3.connect('movedFiles.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_mtime) VALUES (?)", \
                        (str.split(i)))
            conn.commit()
        conn.close()
    

            
    
        


        
        




if __name__ == "__main__":
    pass
