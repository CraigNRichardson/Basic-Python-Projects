import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
import shutil
import fnmatch
import pathlib
import time
import glob
import sqlite3

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

def checkfiles(self):
    src = self.FileBrowse1.get()
    dst = self.FileBrowse2.get()
    seconds_in_24hrs = 24 * 60 * 60
    now = time.time()
    then = now - seconds_in_24hrs
    
    def last_modified(files):
        return os.path.getmtime(files)
    
    for files in (os.listdir(src)):
        src_files = os.path.join(src, files)
        if last_modified(src_files) > then:
            dst_files = os.path.join(dst, files)
            shutil.move(src_files, dst_files)
            
    fPath = dst
    date_file_list = []
    for folder in glob.glob(fPath):
        print ("folder =", folder)
        for file in glob.glob(folder + '/*.txt'):
            stats = os.stat(file)
            lastmod_date = time.localtime(stats[8])
            date_file_tuple = lastmod_date, file
            date_file_list.append(date_file_tuple)
    date_file_list.sort()
    date_file_list.reverse()

    print ("%-40s %s" % ("filename:", "last modified:"))
    for file in date_file_list:
        folder, file_name = os.path.split(file[1])
        file_date = time.strftime("%m/%d/%y %H:%M:%S", file[0])
        print ("%-40s %s" % (file_name, file_date))

    conn = sqlite3.connect('122.db')
    with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles( \
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                        file_name TEXT, \
                        file_date TEXT \
                        )")

##    def sql_insert(conn, file):
    for file in date_file_list:
##        if file.endswith('*.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_textFiles VALUES (?,?,?)", (None, file_name, file_date))
            conn.commit()
    conn.close
            
    conn = sqlite3.connect('122.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_textFiles")
        varFiles = cur.fetchall()
        for item in varFiles:
            msg = "ID: {} File Name: {} Modified Date: {}".format(item[0],item[1],item[2])
            print(msg)

    conn.close    
        

                    
if __name__ == "__main__":
    pass
