
import csv
filename = "students.csv"
from estd_conn import estd_connection

cursor =estd_connection()

with open(filename, "r") as cr:
    students = csv.DictReader(cr)
    for student in students:
        id =student['id']
        name =student['name']
        age =student['age']
        address =student['address']

        sql= f"""
        INSERT INTO STUDENT (ID,NAME,AGE,ADDRESS) VALUES ('{id}','{name}',{age},'{address}')
        """
        cursor.execute(sql)
print("Loaded SuccessFullly...")