# This file stores database connection settings.
# I am using a .env file so that the real password is not written directly in the code.

import os
from dotenv import load_dotenv

# Load values from the .env file
load_dotenv()

def get_connection_details():
    # Database name
    db_name = os.getenv("DB_NAME")

    # PostgreSQL username
    db_user = os.getenv("DB_USER")

    # PostgreSQL password
    db_password = os.getenv("DB_PASSWORD")

    # PostgreSQL host, usually localhost for local computer
    db_host = os.getenv("DB_HOST")

    # PostgreSQL port, usually 5432
    db_port = os.getenv("DB_PORT")

    return {
        "dbname": db_name,
        "user": db_user,
        "password": db_password,
        "host": db_host,
        "port": db_port
    }
