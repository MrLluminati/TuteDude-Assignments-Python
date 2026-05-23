# Simple menu app to add, view, update, and delete students.

from psycopg import Error

from db_setup import create_students_table
from student_crud import (
    add_student,
    delete_student,
    get_all_students,
    get_student_by_id,
    print_students,
    update_student_marks,
)


def read_int(prompt):
    # Keep asking until the user types a valid whole number
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    try:
        create_students_table()

        while True:
            print("\nStudent Management Menu")
            print("1. Add student")
            print("2. View all students")
            print("3. View student by ID")
            print("4. Update student marks")
            print("5. Delete student")
            print("6. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                name = input("Name: ").strip()
                email = input("Email: ").strip()
                course = input("Course: ").strip()
                marks = read_int("Marks: ")
                student_id = add_student(name, email, course, marks)
                print("Saved with ID", student_id)

            elif choice == "2":
                print_students(get_all_students())

            elif choice == "3":
                student_id = read_int("Enter student ID: ")
                row = get_student_by_id(student_id)
                if row is None:
                    print("Student not found.")
                else:
                    print_students([row])

            elif choice == "4":
                student_id = read_int("Enter student ID: ")
                marks = read_int("Enter new marks: ")
                if update_student_marks(student_id, marks):
                    print("Marks updated.")
                else:
                    print("Student not found.")

            elif choice == "5":
                student_id = read_int("Enter student ID to delete: ")
                if delete_student(student_id):
                    print("Student deleted.")
                else:
                    print("Student not found.")

            elif choice == "6":
                print("Goodbye.")
                break

            else:
                print("Invalid choice. Enter 1 to 6.")

    except Error as error:
        print("Database error:", error)


if __name__ == "__main__":
    main()
