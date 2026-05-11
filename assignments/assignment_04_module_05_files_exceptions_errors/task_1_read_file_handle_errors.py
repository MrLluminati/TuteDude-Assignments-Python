"""Task 1: Read a file and handle missing-file errors."""

from pathlib import Path


def read_file_lines(file_path):
    """Return the lines from file_path, or None if the file is missing."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return None


def main():
    file_path = Path(__file__).with_name("sample.txt")
    lines = read_file_lines(file_path)

    if lines is None:
        print("Error: The file 'sample.txt' was not found.")
        return

    print("Reading file content:")

    for line in lines:
        print(line.rstrip())


if __name__ == "__main__":
    main()
