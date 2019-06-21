import pymysql
#连接本地test数据库
db = pymysql.connect(host="localhost", user="lin",
 	password="12580", db="test", port=3306)

#使用cursor()方法创建一个游标对象
cursor = db.cursor()
#使用execute()方法执行SQL语句
cursor.execute("show databases")
#使用fetall()获取全部数据
data = cursor.fetchall()
#打印获取到的数据
print(data)

import pymysql

db = pymysql.connect(host="localhost", user="lin", password="12580", db="12580", port="3306")
cursor = db.cursor()
cursor.execute("")
data = cursor.fetchall()
print(data)