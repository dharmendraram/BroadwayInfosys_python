# delete.py
from estb_conn import connection


def delete_student():
    conn = connection()
    if conn is None:
        return False

    id = input("Enter student ID to delete: ")

    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM student WHERE id = %s", (id,))
            conn.commit()
            print("Student deleted successfully.")
        except Exception as e:
            print(f"Failed to delete student: {e}")
            conn.rollback()

    conn.close()
    return input("Delete another student? (y/n): ").lower() == 'y'
