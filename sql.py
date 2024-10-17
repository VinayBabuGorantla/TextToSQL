import sqlite3

# Connect to sqlite
connection=sqlite3.connect("student.db")

# Create cursor object to insert record, create table and retrieve data
cursor=connection.cursor()

# Create table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

# Insert some records
cursor.execute('''Insert Into STUDENT values('Vinay','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Babu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Gorantla','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Hemanth','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Shiva','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
