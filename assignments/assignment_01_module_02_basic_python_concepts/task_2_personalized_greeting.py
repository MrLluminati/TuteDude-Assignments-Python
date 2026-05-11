"""Task 2: Create a personalized greeting."""


def read_name(prompt):
    """Read a non-empty name from the user."""
    while True:
        name = input(prompt).strip()

        if name:
            return name

        print("This field cannot be empty.")


def main():
    first_name = read_name("Enter your first name: ")
    last_name = read_name("Enter your last name: ")
    full_name = f"{first_name} {last_name}"

    print(f"\nHello, {full_name}! Welcome to the Python program.")


if __name__ == "__main__":
    main()
