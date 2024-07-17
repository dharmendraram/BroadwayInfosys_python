# create.py
from estb_conn import connection


def create_student():
    conn = connection()
    if conn is None:
        return False
    id = input("Enter students id: ")
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    age = input("Enter student age: ")

    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO student (id,name,address, age) VALUES (%s,%s,%s, %s)", (id,name,address,age))
            conn.commit()
            print("Student created successfully.")
        except Exception as e:
            print(f"Failed to create student: {e}")
            conn.rollback()

    conn.close()
    return input("Create another student? (y/n): ").lower() == 'y'
