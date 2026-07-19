from pathlib import Path
import os
from urllib.parse import quote_plus

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


DB_SERVER = os.getenv("DB_SERVER", "localhost\\SQLEXPRESS")
DB_NAME = os.getenv("DB_NAME", "RetailIntelligenceDW")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_AUTH_MODE = os.getenv("DB_AUTH_MODE", "windows").lower()
DB_USERNAME = os.getenv("DB_USERNAME", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_TRUST_SERVER_CERTIFICATE = os.getenv("DB_TRUST_SERVER_CERTIFICATE", "yes")


def get_odbc_connection_string() -> str:
    """
    Build ODBC connection string for SQL Server.
    Supports Windows Authentication and SQL Server Authentication.
    """

    connection_parts = [
        f"DRIVER={{{DB_DRIVER}}}",
        f"SERVER={DB_SERVER}",
        f"DATABASE={DB_NAME}",
        "Encrypt=yes",
        f"TrustServerCertificate={DB_TRUST_SERVER_CERTIFICATE}",
    ]

    if DB_AUTH_MODE == "windows":
        connection_parts.append("Trusted_Connection=yes")
    elif DB_AUTH_MODE == "sql":
        connection_parts.append(f"UID={DB_USERNAME}")
        connection_parts.append(f"PWD={DB_PASSWORD}")
    else:
        raise ValueError("DB_AUTH_MODE must be either 'windows' or 'sql'.")

    return ";".join(connection_parts) + ";"


def get_sqlalchemy_connection_url() -> str:
    """
    Build SQLAlchemy connection URL using pyodbc.
    """

    odbc_connection_string = get_odbc_connection_string()
    encoded_connection_string = quote_plus(odbc_connection_string)

    return f"mssql+pyodbc:///?odbc_connect={encoded_connection_string}"