# This file creates the students table in PostgreSQL.

import psycopg
from db_config import get_connection_details

def create_table():
    connection = psycopg.connect(**get_connection_details())
    cursor = connection.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        course VARCHAR(100)
    );
    """

    print("Running this SQL:")
    print(sql)

    cursor.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()

    print("students table created successfully.")

if __name__ == "__main__":
    create_table()
