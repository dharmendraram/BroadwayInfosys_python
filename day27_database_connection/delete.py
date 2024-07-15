from estd_conn import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")

sql = f"""
DELETE FROM STUDENT WHERE ID='{id}'
"""

cursor.execute(sql)
print("Student Deleted Successfully")