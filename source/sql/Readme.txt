import sqlite3
conn = sqlite3.connect("数据库位置")
cu=conn.cursor()
# 创建一张user表，表中有id(主键),名字(唯一),年龄,备注(默认为空)
cu.execute("create table user (id integer primary key,name varchar(20) UNIQUE,age integer,comment text NULL)")
#增
for user in[(0,'aaa',111,'aaaa'),(1,'bbb',222,'bbbb')]:
 conn.execute("insert into user values (?,?,?,?)", user) # 注意user是元组，不可变
conn.commit() # 注意插入操作之后要进行提交
#查
cu.execute("select * from user")
cu.fetchone() # 得到游标的第一个值
cu.execute("select * from user")
cu.fetchall() # 使用游标的fetch函数,fetchall得到所有的查询记录
#改
cu.execute("update user set name='ccc' where id = 0")
conn.commit()
#删
cu.execute("delete from user where id = 1")
conn.commit()
