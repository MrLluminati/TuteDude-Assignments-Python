"""PostgreSQL CRUD practical for Assignment 7."""

from __future__ import annotations

from typing import Iterable

import psycopg
from psycopg.rows import dict_row

from db_config import get_database_config


class StudentRepository:
    """Repository class containing CRUD methods for the students table."""

    def __init__(self) -> None:
        self.config = get_database_config()

    def _connect(self):
        return psycopg.connect(**self.config.as_dsn_kwargs())

    def add_student(self, name: str, email: str, course: str, marks: int) -> int:
        query = """
            INSERT INTO students (name, email, course, marks)
            VALUES (%s, %s, %s, %s)
            RETURNING student_id;
        """
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (name, email, course, marks))
                return cursor.fetchone()[0]

    def fetch_all_students(self) -> list[dict[str, object]]:
        query = """
            SELECT student_id, name, email, course, marks, created_at
            FROM students
            ORDER BY student_id;
        """
        with self._connect() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(query)
                return list(cursor.fetchall())

    def fetch_student_by_id(self, student_id: int) -> dict[str, object] | None:
        query = """
            SELECT student_id, name, email, course, marks, created_at
            FROM students
            WHERE student_id = %s;
        """
        with self._connect() as connection:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(query, (student_id,))
                return cursor.fetchone()

    def update_marks(self, student_id: int, marks: int) -> bool:
        query = "UPDATE students SET marks = %s WHERE student_id = %s;"
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (marks, student_id))
                return cursor.rowcount > 0

    def delete_student(self, student_id: int) -> bool:
        query = "DELETE FROM students WHERE student_id = %s;"
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (student_id,))
                return cursor.rowcount > 0


def print_students(students: Iterable[dict[str, object]]) -> None:
    students = list(students)
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 80)
    for student in students:
        print(
            f"ID: {student['student_id']} | "
            f"Name: {student['name']} | "
            f"Email: {student['email']} | "
            f"Course: {student['course']} | "
            f"Marks: {student['marks']}"
        )
    print("-" * 80)


def run_demo() -> None:
    repository = StudentRepository()

    print("Adding sample students...")
    first_id = repository.add_student("Aarav Sharma", "aarav@example.com", "Python", 88)
    second_id = repository.add_student("Meera Singh", "meera@example.com", "Python", 92)
    print(f"Inserted student IDs: {first_id}, {second_id}")

    print_students(repository.fetch_all_students())

    print(f"\nFetching student with ID {first_id}...")
    print(repository.fetch_student_by_id(first_id))

    print(f"\nUpdating marks for student ID {first_id}...")
    if repository.update_marks(first_id, 95):
        print("Marks updated successfully.")
    else:
        print("Student not found. Marks were not updated.")

    print_students(repository.fetch_all_students())

    print(f"\nDeleting student with ID {second_id}...")
    if repository.delete_student(second_id):
        print("Student deleted successfully.")
    else:
        print("Student not found. Nothing was deleted.")

    print_students(repository.fetch_all_students())


if __name__ == "__main__":
    run_demo()
