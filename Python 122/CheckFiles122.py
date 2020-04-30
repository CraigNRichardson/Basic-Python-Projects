from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Check files')
        self.master.config(bg='white')

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=10, pady=(20,0), sticky=NW)

        self.FileBrowse1 = Entry(self.master, font=("Helvetica", 16), fg='black', bg='white')
        self.FileBrowse1.grid(row=0, column=1, padx=(10,10), pady=(20,0))

        self.FileBrowse2 = Entry(self.master, font=("Helvetica", 16), fg='black', bg='white')
        self.FileBrowse2.grid(row=1, column=1, padx=(10,10), pady=(20,0))

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(10,10), pady=(20,0), sticky=NW)

        self.btnCheckFiles = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheckFiles.grid(row=2, column=0, padx=(10,10), pady=(20,0), sticky=NW)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2, column=1, padx=(150,0))

        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
