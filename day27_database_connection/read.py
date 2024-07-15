from estd_conn import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")

read_sql = f"""
SELECT * FROM STUDENT WHERE ID='{id}'
"""

cursor.execute(read_sql)
result = cursor.fetchone()
print(result)