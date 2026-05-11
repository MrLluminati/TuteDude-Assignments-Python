"""Task 1: Calculate factorial using a function."""


def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def read_non_negative_integer(prompt):
    """Read a valid non-negative integer from the user."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if number < 0:
            print("Please enter a non-negative integer.")
            continue

        return number


def main():
    number = read_non_negative_integer("Enter a non-negative integer: ")
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")


if __name__ == "__main__":
    main()
