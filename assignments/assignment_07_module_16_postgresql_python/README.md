# Assignment 7 - PostgreSQL with Python

This assignment connects Python to a PostgreSQL database and performs basic student record operations.

## What this project does

- `db_config.py` reads database login details from a `.env` file.
- `db_setup.py` creates the `students` table.
- `student_crud.py` runs INSERT, SELECT, UPDATE, and DELETE queries and prints the SQL being used.
- `menu_app.py` is a small terminal menu to manage students.

## PostgreSQL setup

1. Install PostgreSQL on your computer.
2. Open pgAdmin or `psql` and create a database named `tutedude_assignment_7`.
3. Copy `.env.example` to `.env`.
4. Put your PostgreSQL username and password inside `.env`.

## Install Python packages

```powershell
pip install -r requirements.txt
```

## How to run

Create the table first:

```powershell
python db_setup.py
```

Expected output:

```text
Database setup completed: students table is ready.
```

Run the CRUD demo:

```powershell
python student_crud.py
```

You should see SQL queries printed for INSERT, SELECT, UPDATE, and DELETE, followed by student rows in the terminal.

Run the menu application:

```powershell
python menu_app.py
```

Use options 1 to 5 to add, view, update, and delete records. Use option 6 to exit.

## Screenshot tips for submission

Take screenshots that show your Python code in the editor and the terminal output together. Capture:

- `db_setup.py` run
- `student_crud.py` run (INSERT and SELECT output visible)
- `menu_app.py` run (add, view, update, delete)

Also include a short personal note (see `LEARNING_NOTE.txt`) explaining what you learned.

## ZIP submission

Do not put your real `.env` file in the ZIP. Submit `.env.example` instead.
