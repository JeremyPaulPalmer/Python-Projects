import sqlite3
import fnmatch

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

desired = '*.txt'
matchingText = fnmatch.filter(fileList, desired)

conn = sqlite3.connect('test2.db')


with conn:
    cur = conn.cursor()
    for i in matchingText:
        cur.execute("INSERT INTO tbl_files(col_files) VALUES (?)", \
                    (str.split(i)))
        conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_files FROM tbl_files")
    varFiles = cur.fetchall()
    print(varFiles)
conn.close()




