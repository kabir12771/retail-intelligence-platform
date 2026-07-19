from sqlalchemy import create_engine, text

from config.database_config import get_sqlalchemy_connection_url


def get_sql_engine():
    """
    Creates and returns a SQLAlchemy engine for SQL Server.
    """
    connection_url = get_sqlalchemy_connection_url()

    engine = create_engine(
        connection_url,
        fast_executemany=True,
        pool_pre_ping=True,
    )

    return engine


def test_sql_connection():
    """
    Tests connection to SQL Server and prints database information.
    """
    engine = get_sql_engine()

    query = text("""
        SELECT
            DB_NAME() AS database_name,
            SUSER_SNAME() AS login_name,
            SYSDATETIME() AS server_datetime;
    """)

    with engine.connect() as connection:
        result = connection.execute(query).fetchone()

    print("SQL Server connection successful.")
    print(f"Database Name: {result.database_name}")
    print(f"Login Name: {result.login_name}")
    print(f"Server DateTime: {result.server_datetime}")

    return True