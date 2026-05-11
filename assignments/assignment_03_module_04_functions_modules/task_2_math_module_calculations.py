"""Task 2: Use the math module for calculations."""

import math


def read_positive_number(prompt):
    """Read a valid positive number from the user."""
    while True:
        value = input(prompt).strip()

        try:
            number = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number <= 0:
            print("Please enter a positive number greater than zero.")
            continue

        return number


def format_number(value):
    """Display whole-number results without a decimal part."""
    if value.is_integer():
        return str(int(value))
    return str(value)


def main():
    number = read_positive_number("Enter a positive number: ")

    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print(f"Square root: {format_number(square_root)}")
    print(f"Natural logarithm: {format_number(natural_log)}")
    print(f"Sine: {format_number(sine_value)}")


if __name__ == "__main__":
    main()
