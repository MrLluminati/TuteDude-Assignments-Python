"""Task 2: Calculate the sum of integers from 1 to 50 using a loop."""


def main():
    total = 0

    for number in range(1, 51):
        total += number

    print(f"The sum of integers from 1 to 50 is: {total}")


if __name__ == "__main__":
    main()
