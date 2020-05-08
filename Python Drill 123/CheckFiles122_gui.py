from tkinter import *
import tkinter as tk

import CheckFiles122
import CheckFiles122_func


def load_gui(self):

    self.btnBrowse1 = Button(self.master, text="Browse...",width=12, height=1,command=lambda: CheckFiles122_func.askdirectory1(self)) 
    self.btnBrowse1.grid(row=0, column=0, padx=10, pady=(20,0), sticky=NW)

    self.FileBrowse1 = Entry(self.master, font=("Helvetica", 16), fg='black', bg='white')
    self.FileBrowse1.grid(row=0, column=1, padx=(10,10), pady=(20,0))

    self.FileBrowse2 = Entry(self.master, font=("Helvetica", 16), fg='black', bg='white')
    self.FileBrowse2.grid(row=1, column=1, padx=(10,10), pady=(20,0))

    self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1,command=lambda: CheckFiles122_func.askdirectory2(self))
    self.btnBrowse2.grid(row=1, column=0, padx=(10,10), pady=(20,0), sticky=NW)

    self.btnCheckFiles = Button(self.master, text="Check for files...", width=12, height=2)
    self.btnCheckFiles.grid(row=2, column=0, padx=(10,10), pady=(20,0), sticky=NW)

    self.btnClose = Button(self.master, text="Close Program", width=12, height=2,command=lambda: CheckFiles122_func.ask_quit(self))
    self.btnClose.grid(row=2, column=1, padx=(150,0))



if __name__ == "__main__":
    pass
