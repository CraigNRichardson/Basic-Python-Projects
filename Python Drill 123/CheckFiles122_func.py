import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog

import CheckFiles122
import CheckFiles122_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def askdirectory1(self):
    directory = tkinter.filedialog.askdirectory()
    directory = str(directory)
    directory = directory.replace('/', '\\')
    self.FileBrowse1.delete(0,END)
    self.FileBrowse1.insert(0,directory)

def askdirectory2(self):
    directory = tkinter.filedialog.askdirectory()
    directory = str(directory)
    directory = directory.replace('/', '\\')
    self.FileBrowse2.delete(0,END)
    self.FileBrowse2.insert(0,directory)

if __name__ == "__main__":
    pass
