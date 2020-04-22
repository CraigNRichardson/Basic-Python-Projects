import sqlite3
import fnmatch


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('104.db')
with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    filename TEXT \
                    )")

def sql_insert(conn, file):
    for file in fileList:
        if fnmatch.fnmatch(file, '*.txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_textFiles VALUES (?)", (file))
                conn.commit()
conn.close
        
conn = sqlite3.connect('104.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_textFiles")
    varFiles = cur.fetchall()
    for item in varFiles:
        msg = "ID: {} File Name: {}".format(item[0],item[1])
    print(msg)

conn.close
