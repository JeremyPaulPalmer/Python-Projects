import os
import webbrowser
from tkinter import *
import tkinter as tk

file_loc = r"C:\python_projects\new_HTML.html"
new = 2

def create_page(self):
    text = tk.Text(self.master, tk.Text)
    with open(file_loc, 'a+') as f:
        f.write("<html>\n<body>\n" + text.get() + "\n</body>\n</html>")
        f.close()

def load_gui(self):

    # Define and place entry boxes
    self.txt_label = tk.Label(self.master, text="Please enter contents of webpage body below:")
    self.txt_label.grid(row=0, column=0, pady=(30,0))
    self.txt_entry = tk.Text(self.master, height=5, width=82)
    self.txt_entry.grid(row=1, column=0, padx=(40,0))

    # Define and place buttons
    self.btn_create = tk.Button(self.master,width=24,height=2,text='Create Webpage',command=lambda:create_page(self))
    self.btn_create.grid(row=2,column=0,ipady=3)


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Frame configuration
        self.master = master
        self.master.minsize(750,275)
        self.master.maxsize(750,275)
        self.master.title("Create HTML file")
        self.master.configure(bg="lightgray")

        load_gui(self)




webbrowser.open(file_loc,new=new)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
