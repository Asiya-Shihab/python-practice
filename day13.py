import sqlite3
conn=sqlite3.connect('practice.db')
cursor=conn.cursor()
cursor.execute("drop table if exists students")
cursor.execute("""create table students(
id integer primary key,
name text,
age integer,
marks integer,branch text)""")
students_data=[(1,"Riya",20,85,'cse'),(2,'Aman',21,45,'ece'),(3,'Zoya',19,92,'cse'),(4,'kabir',22,67,'ece'),(5,'sara',20,78,'cse'),(6,'vikram',23,55,'ece')]
cursor.executemany("insert into students values (?,?,?,?,?)",students_data)
conn.commit()
cursor.execute("select * from students order by marks")
print(cursor.fetchall())
cursor.execute("select * from students order by marks desc")
print(cursor.fetchall())
cursor.execute("select count(*) from students")
print(cursor.fetchall())
cursor.execute("select avg(marks) from students")
print(cursor.fetchall())
cursor.execute("Select max(marks),min(marks) from students")
print(cursor.fetchall())
cursor.execute("select sum(marks) from students")
print(cursor.fetchall())
cursor.execute("Select branch ,count(*) from students group by branch")
print(cursor.fetchall())
cursor.execute("select branch ,avg(marks) from students group by branch")
print(cursor.fetchall())