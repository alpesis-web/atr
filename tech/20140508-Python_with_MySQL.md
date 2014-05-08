May 8 2014 | Python, db | Kelly Chan
# Python with MySQL

example
```python
  
#mysqldb    
import time
import MySQLdb    
   
# connect 
conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")  
cursor = conn.cursor()    
   
# write  
sql = "insert into user(name,created) values(%s,%s)"   
param = ("aaa",int(time.time()))    
n = cursor.execute(sql,param)    
print n    
   
# update   
sql = "update user set name=%s where id=3"   
param = ("bbb")    
n = cursor.execute(sql,param)    
print n    
   
# query
n = cursor.execute("select * from user")    
for row in cursor.fetchall():    
    for r in row:    
        print r    
   
# delete   
sql = "delete from user where name=%s"   
param =("aaa")    
n = cursor.execute(sql,param)    
print n    
cursor.close()    
   
# close   
conn.close()   
```
