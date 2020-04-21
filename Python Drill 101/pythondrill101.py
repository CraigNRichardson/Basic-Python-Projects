import os
import time
import fnmatch
import glob





fPath = 'C:\\Users\\Craig\\Desktop\\python_projects\\Python Drill 101\\Python Drill 101 Assets\\'

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


##for textfiles in os.listdir(fPath):
##    if fnmatch.fnmatch(textfiles, '*.txt'):
##        print(os.path.join(fPath, textfiles),"Last Modified: %s" %time.ctime(os.path.getmtime('C:\\Users\\Craig\\Desktop\\python_projects\\Python Drill 101\\Python Drill 101 Assets\\')))
##
##

##files = list(filter(os.path.isfile, glob.glob(fPath + "*.txt")))
##print(files.sort(key=lambda x: os.path.getmtime(x)))

