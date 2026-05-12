"""Interactive PostgreSQL student management app for Assignment 7."""

from __future__ import annotations

from psycopg import Error

from db_setup import create_students_table
from student_crud import StudentRepository, print_students


def read_int(prompt: str, minimum: int | None = None, maximum: int | None = None) -> int:
    """Read and validate an integer from terminal input."""
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Please enter a value less than or equal to {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_student(repository: StudentRepository) -> None:
    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()
    course = input("Enter course name: ").strip()
    marks = read_int("Enter marks between 0 and 100: ", 0, 100)

    if not name or not email or not course:
        print("Name, email, and course cannot be blank.")
        return

    student_id = repository.add_student(name, email, course, marks)
    print(f"Student added successfully with ID {student_id}.")


def view_student(repository: StudentRepository) -> None:
    student_id = read_int("Enter student ID: ", 1)
    student = repository.fetch_student_by_id(student_id)
    if student is None:
        print("Student not found.")
        return
    print_students([student])


def update_student_marks(repository: StudentRepository) -> None:
    student_id = read_int("Enter student ID: ", 1)
    marks = read_int("Enter new marks between 0 and 100: ", 0, 100)
    if repository.update_marks(student_id, marks):
        print("Student marks updated successfully.")
    else:
        print("Student not found. Marks were not updated.")


def delete_student(repository: StudentRepository) -> None:
    student_id = read_int("Enter student ID to delete: ", 1)
    if repository.delete_student(student_id):
        print("Student deleted successfully.")
    else:
        print("Student not found. Nothing was deleted.")


def main() -> None:
    try:
        create_students_table()
        repository = StudentRepository()

        while True:
            print("\nPostgreSQL Student Management App")
            print("1. Add student")
            print("2. View all students")
            print("3. View student by ID")
            print("4. Update student marks")
            print("5. Delete student")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student(repository)
            elif choice == "2":
                print_students(repository.fetch_all_students())
            elif choice == "3":
                view_student(repository)
            elif choice == "4":
                update_student_marks(repository)
            elif choice == "5":
                delete_student(repository)
            elif choice == "6":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
    except Error as error:
        print("A PostgreSQL error occurred:")
        print(error)


if __name__ == "__main__":
    main()
