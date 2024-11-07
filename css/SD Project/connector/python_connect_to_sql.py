import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='',database='afia19')
my_cursor=conn.cursor()

conn.commit()
conn.close()

printf("connection successfully created!")
