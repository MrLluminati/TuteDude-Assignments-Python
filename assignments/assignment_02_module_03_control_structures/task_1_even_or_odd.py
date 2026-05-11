"""Task 1: Check whether a user-provided integer is even or odd."""


def read_integer(prompt):
    """Read a valid integer from the user."""
    while True:
        value = input(prompt).strip()

        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


def main():
    number = read_integer("Enter an integer: ")

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")


if __name__ == "__main__":
    main()
