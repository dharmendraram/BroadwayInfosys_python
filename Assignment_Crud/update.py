# update.py
from estb_conn import connection

def update_student():
    conn = connection()
    if conn is None:
        return False

    id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    address = input("Enter new address: ")
    age = input("Enter new age: ")

    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE student SET name = %s, address = %s, age = %s WHERE id = %s", (name, address, age, id))
            conn.commit()
            print("Student updated successfully.")
        except Exception as e:
            print(f"Failed to update student: {e}")
            conn.rollback()

    conn.close()
    return input("Update another student? (y/n): ").lower() == 'y'
