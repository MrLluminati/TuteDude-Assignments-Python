# Creates the students table in PostgreSQL.

import psycopg

from db_config import get_db_settings

# SQL to create the table for this assignment
create_table_sql = """
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    course VARCHAR(100) NOT NULL,
    marks INTEGER NOT NULL CHECK (marks >= 0 AND marks <= 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


def create_students_table():
    print("Running SQL:")
    print(create_table_sql)

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(create_table_sql)
    connection.commit()
    cursor.close()
    connection.close()

    print("Database setup completed: students table is ready.")


if __name__ == "__main__":
    create_students_table()
