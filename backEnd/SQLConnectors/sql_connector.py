import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',passwd='aadityabhh',database='esd')

mycursor = mydb.cursor()

mycursor.execute('select max(quantity) from bill1')

result = mycursor.fetchone()

for i in result:
    print(i)
