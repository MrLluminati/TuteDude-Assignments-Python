# Practical file for Assignment 7.
# This file shows INSERT, SELECT, UPDATE, and DELETE using psycopg.

import psycopg

from db_config import get_db_settings

# Demo students use fixed emails so we can run this file more than once
demo_email_1 = "aarav@example.com"
demo_email_2 = "meera@example.com"


def add_student(name, email, course, marks):
    sql = """
        INSERT INTO students (name, email, course, marks)
        VALUES (%s, %s, %s, %s)
        RETURNING student_id;
    """
    values = (name, email, course, marks)

    print("\nRunning INSERT:")
    print(sql.strip())
    print("Values:", values)

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(sql, values)
    student_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()

    print("Inserted student with ID:", student_id)
    return student_id


def get_all_students():
    sql = """
        SELECT student_id, name, email, course, marks
        FROM students
        ORDER BY student_id;
    """

    print("\nRunning SELECT (all students):")
    print(sql.strip())

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return rows


def get_student_by_id(student_id):
    sql = """
        SELECT student_id, name, email, course, marks
        FROM students
        WHERE student_id = %s;
    """
    values = (student_id,)

    print("\nRunning SELECT (one student):")
    print(sql.strip())
    print("Values:", values)

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(sql, values)
    row = cursor.fetchone()
    cursor.close()
    connection.close()

    return row


def update_student_marks(student_id, marks):
    sql = "UPDATE students SET marks = %s WHERE student_id = %s;"
    values = (marks, student_id)

    print("\nRunning UPDATE:")
    print(sql)
    print("Values:", values)

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(sql, values)
    updated_rows = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()

    return updated_rows > 0


def delete_student(student_id):
    sql = "DELETE FROM students WHERE student_id = %s;"
    values = (student_id,)

    print("\nRunning DELETE:")
    print(sql)
    print("Values:", values)

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(sql, values)
    deleted_rows = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()

    return deleted_rows > 0


def delete_demo_students():
    # Remove old demo rows so the script can run again without duplicate email error
    sql = "DELETE FROM students WHERE email = %s OR email = %s;"
    values = (demo_email_1, demo_email_2)

    print("\nCleaning old demo records (if any)...")
    print(sql)
    print("Values:", values)

    connection = psycopg.connect(**get_db_settings())
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()


def print_students(rows):
    if not rows:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 70)
    for row in rows:
        student_id, name, email, course, marks = row
        print(
            f"ID: {student_id} | Name: {name} | Email: {email} | "
            f"Course: {course} | Marks: {marks}"
        )
    print("-" * 70)


def run_demo():
    delete_demo_students()

    print("\n=== CREATE (INSERT) ===")
    first_id = add_student("Aarav Sharma", demo_email_1, "Python", 88)
    second_id = add_student("Meera Singh", demo_email_2, "Python", 92)

    print("\n=== READ (SELECT all) ===")
    print_students(get_all_students())

    print("\n=== READ (SELECT one) ===")
    one_student = get_student_by_id(first_id)
    print("Fetched row:", one_student)

    print("\n=== UPDATE ===")
    if update_student_marks(first_id, 95):
        print("Marks updated successfully.")
    else:
        print("Student not found.")

    print_students(get_all_students())

    print("\n=== DELETE ===")
    if delete_student(second_id):
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    print_students(get_all_students())


if __name__ == "__main__":
    run_demo()
