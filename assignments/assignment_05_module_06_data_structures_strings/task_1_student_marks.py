"""Task 1: Create a dictionary of student marks."""


STUDENT_MARKS = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 81,
}


def read_student_name(prompt):
    """Read a non-empty student name from the user."""
    while True:
        name = input(prompt).strip()

        if name:
            return name

        print("Please enter a student name.")


def find_marks(student_name):
    """Return marks for a student using case-insensitive lookup."""
    for name, marks in STUDENT_MARKS.items():
        if name.lower() == student_name.lower():
            return name, marks

    return None, None


def main():
    student_name = read_student_name("Enter the student's name: ")
    matched_name, marks = find_marks(student_name)

    if matched_name is None:
        print(f"No marks found for {student_name}.")
    else:
        print(f"{matched_name}'s marks: {marks}")


if __name__ == "__main__":
    main()
