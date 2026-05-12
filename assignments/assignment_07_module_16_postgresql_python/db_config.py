"""Database configuration helper for Assignment 7.

This module reads PostgreSQL connection details from environment variables.
Create a local .env file from .env.example before running the scripts.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class DatabaseConfig:
    """PostgreSQL connection configuration."""

    dbname: str
    user: str
    password: str
    host: str = "localhost"
    port: int = 5432

    def as_dsn_kwargs(self) -> dict[str, object]:
        """Return values in the keyword format expected by psycopg2.connect."""
        return {
            "dbname": self.dbname,
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port,
        }


def get_database_config() -> DatabaseConfig:
    """Read database configuration from environment variables."""
    return DatabaseConfig(
        dbname=os.getenv("DB_NAME", "tutedude_assignment_7"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
    )
