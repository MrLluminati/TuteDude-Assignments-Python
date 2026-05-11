"""Task 1: Perform basic mathematical operations on two numbers."""


def read_number(prompt):
    """Read a valid number from the user."""
    while True:
        value = input(prompt).strip()

        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def format_number(value):
    """Display whole numbers without a decimal part."""
    if value.is_integer():
        return str(int(value))
    return str(value)


def main():
    first_number = read_number("Enter the first number: ")
    second_number = read_number("Enter the second number: ")

    print("\nResults:")
    print(f"Addition: {format_number(first_number + second_number)}")
    print(f"Subtraction: {format_number(first_number - second_number)}")
    print(f"Multiplication: {format_number(first_number * second_number)}")

    if second_number == 0:
        print("Division: Cannot divide by zero")
    else:
        print(f"Division: {format_number(first_number / second_number)}")


if __name__ == "__main__":
    main()
