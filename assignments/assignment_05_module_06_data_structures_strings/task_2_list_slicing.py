"""Task 2: Demonstrate list slicing."""


def main():
    numbers = list(range(1, 11))
    first_five = numbers[:5]
    reversed_first_five = first_five[::-1]

    print(f"Original list: {numbers}")
    print(f"First five elements: {first_five}")
    print(f"Reversed first five elements: {reversed_first_five}")


if __name__ == "__main__":
    main()
