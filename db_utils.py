# db_utils.py
import mysql.connector

def fetch_all_patients():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Saleem@123#',
        database='patient_database'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, gender, story FROM patient_entries")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
