from tkinter import *
import tkinter as tk

import CheckFiles122_gui
import CheckFiles122b_func

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Check files')
        self.master.config(bg='white')

        self.master.protocol("WM_DELETE_WINDOW", lambda: CheckFiles122b_func.ask_quit(self))
        arg = self.master

        CheckFiles122_gui.load_gui(self)

            
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

