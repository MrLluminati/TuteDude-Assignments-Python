# Reads PostgreSQL login details from the .env file.
# Copy .env.example to .env and put your real password there.

import os

from dotenv import load_dotenv

load_dotenv()


def get_db_settings():
    """Return a dictionary that psycopg.connect() can use."""

    # Name of the database created in pgAdmin or psql
    dbname = os.getenv("DB_NAME", "tutedude_assignment_7")

    # PostgreSQL username (usually postgres on a local PC)
    user = os.getenv("DB_USER", "postgres")

    # Password you set during PostgreSQL installation
    password = os.getenv("DB_PASSWORD", "")

    # Where PostgreSQL is running (localhost means this computer)
    host = os.getenv("DB_HOST", "localhost")

    # Default PostgreSQL port
    port = int(os.getenv("DB_PORT", "5432"))

    return {
        "dbname": dbname,
        "user": user,
        "password": password,
        "host": host,
        "port": port,
    }
