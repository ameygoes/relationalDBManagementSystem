import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',passwd='aadityabhh',database='employees')

mycursor = mydb.cursor()

mycursor.execute('select * from departments')

result = mycursor.fetchall()

for i in result:
    print(i)
