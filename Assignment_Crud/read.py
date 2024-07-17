# read.py
from estb_conn import connection


def read_student():
    conn = connection()
    if conn is None:
        return False

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f"Failed to read students: {e}")

    conn.close()
    return input("Read more students? (y/n): ").lower() == 'y'
