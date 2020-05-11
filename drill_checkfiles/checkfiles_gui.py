from tkinter import *
import tkinter as tk


# Import main
import checkfiles_main



def load_gui(self):

    # Define and place entry boxes
    self.txt_browse1 = tk.Entry(self.master,text='', width=82)
    self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=5,padx=(25,0),pady=(60,0))
    self.txt_browse2 = tk.Entry(self.master,text='', width=82)
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=5,padx=(25,0),pady=(20,0))

    # Define and place buttons
    self.btn_browse1 = tk.Button(self.master,width=24,height=2,text='Browse...')
    self.btn_browse1.grid(row=0,column=0,padx=(25,0),pady=(60,0))
    self.btn_browse2 = tk.Button(self.master,width=24,height=2,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(20,0))
    self.btn_check = tk.Button(self.master,width=24,height=4,text='Check for files...')
    self.btn_check.grid(row=2,column=0,padx=(25,0),pady=(20,0))
    self.btn_close = tk.Button(self.master,width=24,height=4,text='Close Program')
    self.btn_close.grid(row=2,column=5,padx=(0,0),pady=(0,0),sticky=S+E)

    

    







if __name__ == "__main__":
    pass
