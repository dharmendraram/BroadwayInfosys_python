
from estd_conn import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")
name = input("Student name ")
age = int(input("Enter student's age "))
address = input("Enter student's address ")

insert_sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', {age}, '{address}')
"""

cursor.execute(insert_sql)
print("Student added successfully !!")