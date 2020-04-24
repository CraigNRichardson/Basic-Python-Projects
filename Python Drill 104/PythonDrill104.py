import sqlite3
import fnmatch


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('104b.db')
with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    filename TEXT \
                    )")

cur.executemany("INSERT INTO tbl_textFiles (filename) VALUES (?)",
                [(filename,) for filename in fileList if filename.endswith(".txt")])
conn.commit()
conn.close

for file in fileList:
    if fnmatch.fnmatch(file, "*.txt"):
        print(file)
        
