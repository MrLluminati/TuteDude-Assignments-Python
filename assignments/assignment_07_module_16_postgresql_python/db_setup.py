"""Create the PostgreSQL table required for Assignment 7."""

from __future__ import annotations

import psycopg2
from psycopg2 import sql

from db_config import get_database_config


CREATE_STUDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    course VARCHAR(100) NOT NULL,
    marks INTEGER NOT NULL CHECK (marks >= 0 AND marks <= 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


def create_students_table() -> None:
    """Create the students table if it does not already exist."""
    config = get_database_config()

    with psycopg2.connect(**config.as_dsn_kwargs()) as connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_STUDENTS_TABLE)

    print("Database setup completed: students table is ready.")


if __name__ == "__main__":
    create_students_table()
