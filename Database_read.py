import sqlite3
conn = sqlite3.connect("C:/Users/pc_01/Desktop/Http_server/source/django/001/my_bbs/db.sqlite3")
cu=conn.cursor()
cu.execute("PRAGMA table_info(post_comment);")
dir=cu.fetchall()
print(dir)