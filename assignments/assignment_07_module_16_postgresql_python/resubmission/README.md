# Assignment 7 Resubmission - PostgreSQL with Python

## Why I am resubmitting

My earlier Assignment 7 submission was rejected because the code and screenshots did not clearly show my own learning process. The mentor specifically asked me to simplify the implementation, avoid overly professional patterns, show the Python code files beside the terminal output, and explain what I learned in my own words.

This resubmission is being rebuilt step by step in a beginner-friendly style.

## Files in this resubmission

- `db_config.py` - reads PostgreSQL connection details from `.env`
- `db_setup.py` - creates the `students` table
- `student_crud.py` - will contain simple INSERT, SELECT, UPDATE, and DELETE functions
- `menu_app.py` - will contain a simple menu-based program
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

## Progress checklist

- [x] Step 1: Database configuration and table setup
- [ ] Step 2: Simple student CRUD operations
- [ ] Step 3: Simple menu application
- [ ] Step 4: Personal learning note
- [ ] Step 5: Final testing and packaging
