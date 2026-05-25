# Assignment 7 Resubmission - PostgreSQL with Python

## Why I am resubmitting

My earlier Assignment 7 submission was rejected because the code and screenshots did not clearly show my own learning process. The mentor specifically asked me to simplify the implementation, avoid overly professional patterns, show the Python code files beside the terminal output, and explain what I learned in my own words.

This resubmission is being rebuilt step by step in a beginner-friendly style. I am documenting the errors, fixes, code, and terminal output together so that the learning process is visible.

## Files in this resubmission

- `db_config.py` - reads PostgreSQL connection details from `.env`
- `db_setup.py` - creates the `students` table
- `student_crud.py` - contains simple INSERT, SELECT, UPDATE, and DELETE functions
- `menu_app.py` - contains a simple menu-based program
- `.env.example` - sample environment file without the real password
- `requirements.txt` - required Python packages
- `LEARNING_NOTE.txt` - personal note about what I learned
- `screenshot_proofs/` - step-wise screenshots showing code and terminal output

## Important note about `.env`

The `.env` file contains the real PostgreSQL password, so it is not included for submission or GitHub. Only `.env.example` is included.

---

## Step 1 - Database configuration and table setup

### What I did

In this step, I created a basic database setup structure.

I created:

- `requirements.txt`
- `.env.example`
- `db_config.py`
- `db_setup.py`

The purpose of `db_config.py` is to read database connection details from the `.env` file. The purpose of `db_setup.py` is to connect Python with PostgreSQL and create the `students` table.

### Files created in Step 1

#### `requirements.txt`

```text
psycopg[binary]
python-dotenv
```

#### `.env.example`

```text
DB_NAME=tutedude_assignment_7
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

#### `db_config.py`

This file uses `load_dotenv()` and `os.getenv()` to read database details.

#### `db_setup.py`

This file connects to PostgreSQL and runs this SQL command:

```sql
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    course VARCHAR(100)
);
```

### Debugging note

At first, I received a PostgreSQL password authentication error. I understood that the code was reaching PostgreSQL, but the password in `.env` was not correct. After correcting the password in `.env`, the table setup command worked successfully.

### Successful terminal output

```text
Running this SQL:

CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    course VARCHAR(100)
);

students table created successfully.
```

### What I learned

- `.env` is used to keep private database details outside the Python code.
- `.env.example` is safe to share because it does not contain the real password.
- `python-dotenv` loads values from the `.env` file.
- `psycopg.connect()` connects Python to PostgreSQL.
- `cursor.execute()` runs SQL from Python.
- `connection.commit()` saves database changes.
- `cursor.close()` and `connection.close()` close the database connection safely.

### Screenshot proof

- [db_config.py code](screenshot_proofs/step_01_db_config_and_setup/step_01_a_db_config_code.png)
- [db_setup.py code](screenshot_proofs/step_01_db_config_and_setup/step_01_b_db_setup_code.png)
- [successful db_setup.py terminal output](screenshot_proofs/step_01_db_config_and_setup/step_01_c_successful_db_setup_output.png)

---

## Step 2 - Simple student CRUD operations

### What I did

In this step, I created `student_crud.py` to perform the four basic database operations:

- `INSERT` - add a new student record
- `SELECT` - view student records
- `UPDATE` - change an existing student record
- `DELETE` - remove a student record

I used simple functions instead of classes or repository patterns:

- `add_student()`
- `view_students()`
- `update_student()`
- `delete_student()`

Each function connects to PostgreSQL, creates a cursor, runs one SQL command, commits if needed, and then closes the cursor and connection.

### SQL commands used

#### INSERT

```sql
INSERT INTO students (name, age, course) VALUES (%s, %s, %s) RETURNING id;
```

This adds a student and returns the newly created student id.

#### SELECT

```sql
SELECT id, name, age, course FROM students ORDER BY id;
```

This reads student records from the table.

#### UPDATE

```sql
UPDATE students SET course = %s WHERE id = %s;
```

This updates the course of the inserted student.

#### DELETE

```sql
DELETE FROM students WHERE id = %s;
```

This deletes the same student record.

### Debugging note

During testing, I first received this error:

```text
psycopg.errors.UndefinedColumn: column "age" of relation "students" does not exist
```

I learned that `CREATE TABLE IF NOT EXISTS` does not change an old table if the table already exists. My old `students` table had a different structure, so the new `age` column was missing.

To fix this, I dropped or truncated the old table and recreated the table using `db_setup.py`. I also used:

```sql
TRUNCATE TABLE students RESTART IDENTITY;
```

This cleared old test records and restarted the id numbering from 1 for a clean demonstration.

### Important correction made in Step 2

At first, I tried using a fixed student id like `1` for update and delete. That caused a problem when the inserted student received a different id.

To fix it, I used `RETURNING id` in the INSERT query and stored the inserted id in this variable:

```python
current_student_id = None
```

After inserting the row, I used:

```python
inserted_row = cursor.fetchone()
current_student_id = inserted_row[0]
```

Then `update_student()` and `delete_student()` used the same `current_student_id`. This made the INSERT, UPDATE, and DELETE operations work on the same student record.

### Successful output summary

The clean final run showed:

```text
Inserted student id: 1

Student Records:
(1, 'Abhijeet Kumar', 25, 'Python')

Student updated successfully.

Student Records:
(1, 'Abhijeet Kumar', 25, 'PostgreSQL with Python')

Student deleted successfully.

Student Records:
```

The final `Student Records:` output was empty, showing that the delete operation worked.

### What I learned

- Parameterized queries use `%s` placeholders and pass actual values separately.
- `RETURNING id` can be used in PostgreSQL to get the id of a newly inserted row.
- `fetchone()` reads one returned row from the cursor.
- `fetchall()` reads all selected rows from the cursor.
- `INSERT`, `UPDATE`, and `DELETE` need `connection.commit()` to save changes.
- `SELECT` is used to check whether the database operation worked.
- Old database tables can cause errors if their structure does not match the current Python code.
- Screenshots should show both the Python code and terminal output so the working process is clear.

### Screenshot proof

- [student_crud.py INSERT code and output](screenshot_proofs/step_02_student_crud_operations/step_02_a_student_crud_insert_code_and_output.png)
- [student_crud.py view/update code and output](screenshot_proofs/step_02_student_crud_operations/step_02_b_student_crud_view_update_code_and_output.png)
- [student_crud.py update code and clean output](screenshot_proofs/step_02_student_crud_operations/step_02_c_student_crud_update_code_and_clean_output.png)
- [student_crud.py delete code and final empty SELECT](screenshot_proofs/step_02_student_crud_operations/step_02_d_student_crud_delete_code_and_final_empty_select.png)
- [debugging screenshot showing missing age column error](screenshot_proofs/step_02_student_crud_operations/step_02_e_debug_age_column_missing_error.png)

---

## Step 3 - Simple menu application

### What I did

In this step, I created `menu_app.py`. The purpose of this file is to give the user a simple text menu for running the database operations from `student_crud.py`.

The menu imports these functions:

- `add_student()`
- `view_students()`
- `update_student()`
- `delete_student()`

The menu then asks the user to select an option from 1 to 5.

### Menu options

```text
Student Database Menu
1. Add student
2. View students
3. Update student
4. Delete student
5. Exit
```

### How the menu works

The program uses a `while True` loop so that the menu keeps appearing after each operation. The loop stops only when the user selects option `5`.

The program uses this line to take user input:

```python
choice = int(input("Enter your choice: "))
```

Since the input is converted into an integer, I used `try` and `except ValueError` to handle non-number input.

### Input validation used

If the user enters text instead of a number, the program prints:

```text
Please enter a number only.
```

If the user enters a number outside 1 to 5, the program prints:

```text
Invalid choice. Please select from 1 to 5.
```

This keeps the menu from crashing when the wrong input is entered.

### Successful menu test flow

I tested this flow:

```text
1 -> Add student
2 -> View students
3 -> Update student
2 -> View updated student
4 -> Delete student
2 -> Confirm final empty records
5 -> Exit
```

The terminal output showed that the menu successfully called the CRUD functions from `student_crud.py`.

### What I learned

- A menu program can call functions from another Python file using `import`.
- `while True` can be used to keep a menu running until the user exits.
- `break` exits the loop.
- `continue` skips the rest of the current loop and shows the menu again.
- `try` and `except ValueError` prevent the program from crashing when the user enters non-number input.
- The menu file should be simple and should only decide which function to call.
- The actual database work remains inside `student_crud.py`.

### Screenshot proof

- [menu_app.py add/view code and output](screenshot_proofs/step_03_menu_app/step_03_a_menu_app_add_and_view_code_output.png)
- [menu_app.py update/delete code and output](screenshot_proofs/step_03_menu_app/step_03_b_menu_app_update_delete_code_output.png)
- [menu_app.py invalid input and exit output](screenshot_proofs/step_03_menu_app/step_03_c_menu_app_invalid_input_and_exit_output.png)

---

## Progress checklist

- [x] Step 1: Database configuration and table setup
- [x] Step 2: Simple student CRUD operations
- [x] Step 3: Simple menu application
- [ ] Step 4: Personal learning note
- [ ] Step 5: Final testing and packaging
