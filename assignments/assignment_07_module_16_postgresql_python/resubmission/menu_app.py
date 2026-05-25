# This file gives a simple menu to run student database operations.

from student_crud import add_student
from student_crud import view_students
from student_crud import update_student
from student_crud import delete_student

# Function to display the menu options
def show_menu():
    print("\nStudent Database Menu")
    print("1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

# Main loop to run the menu
while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number only.")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")