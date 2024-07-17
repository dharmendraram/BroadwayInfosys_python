
import psycopg2
def connection():
    conn = psycopg2.connect(
        database="studentdb",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port=5432
    )
    return conn
