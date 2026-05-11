"""Task 2: Write, append, and read data from a file."""

from pathlib import Path


def main():
    output_path = Path(__file__).with_name("output.txt")

    first_entry = input("Enter text to write to the file: ").strip()
    second_entry = input("Enter additional text to append: ").strip()

    with output_path.open("w", encoding="utf-8") as file:
        file.write(first_entry + "\n")

    with output_path.open("a", encoding="utf-8") as file:
        file.write(second_entry + "\n")

    print("\nFinal content of output.txt:")

    with output_path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())


if __name__ == "__main__":
    main()
