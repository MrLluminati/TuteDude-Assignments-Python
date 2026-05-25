# This file performs basic CRUD operations on the students table.
# CRUD means Create, Read, Update, and Delete.

import psycopg
from db_config import get_connection_details


# This variable will store the id of the student inserted by add_student().
# I am using this so that update_student() and delete_student()
# work on the same student record.
current_student_id = None


def add_student():
    global current_student_id

    # INSERT means adding a new row into the table.
    name = "Abhijeet Kumar"
    age = 25
    course = "Python"

    # RETURNING id gives back the id of the newly inserted student.
    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s) RETURNING id;"

    print("Running INSERT query:")
    print(sql)
    print("Values:", name, age, course)

    connection = psycopg.connect(**get_connection_details())
    cursor = connection.cursor()

    cursor.execute(sql, (name, age, course))

    # fetchone() gets the returned id from PostgreSQL.
    inserted_row = cursor.fetchone()
    current_student_id = inserted_row[0]

    connection.commit()

    cursor.close()
    connection.close()

    print("Student inserted successfully.")
    print("Inserted student id:", current_student_id)


def view_students():
    # SELECT means reading rows from the table.
    sql = "SELECT id, name, age, course FROM students ORDER BY id;"

    print("\nRunning SELECT query:")
    print(sql)

    connection = psycopg.connect(**get_connection_details())
    cursor = connection.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    print("\nStudent Records:")
    for row in rows:
        print(row)

    cursor.close()
    connection.close()


def update_student():
    global current_student_id

    # UPDATE means changing existing data.
    student_id = current_student_id
    new_course = "PostgreSQL with Python"

    sql = "UPDATE students SET course = %s WHERE id = %s;"

    print("\nRunning UPDATE query:")
    print(sql)
    print("Values:", new_course, student_id)

    connection = psycopg.connect(**get_connection_details())
    cursor = connection.cursor()

    cursor.execute(sql, (new_course, student_id))
    connection.commit()

    cursor.close()
    connection.close()

    print("Student updated successfully.")


def delete_student():
    global current_student_id

    # DELETE means removing a row from the table.
    student_id = current_student_id

    sql = "DELETE FROM students WHERE id = %s;"

    print("\nRunning DELETE query:")
    print(sql)
    print("Value:", student_id)

    connection = psycopg.connect(**get_connection_details())
    cursor = connection.cursor()

    cursor.execute(sql, (student_id,))
    connection.commit()

    cursor.close()
    connection.close()

    print("Student deleted successfully.")


if __name__ == "__main__":
    add_student()
    view_students()
    update_student()
    view_students()
    delete_student()
    view_students()