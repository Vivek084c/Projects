import contextlib

class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection

    def commit(self):
        print("Transaction committed.")
        self.connection.commit()

    def rollback(self):
        print("Transaction rolled back.")
        self.connection.rollback()


@contextlib.contextmanager
def transaction_manager(connection):
    """
    Context manager to handle database transactions.
    Commits the transaction if no exception occurs, otherwise rolls it back.
    """
    transaction = DatabaseTransaction(connection)
    try:
        yield transaction
        transaction.commit()  # Commit the transaction when leaving the context
    except Exception as e:
        transaction.rollback()  # Rollback if there's an exception
        raise  # Re-raise the exception after rollback

# Example usage
import sqlite3

# Assume we have a SQLite database connection
connection = sqlite3.connect("example.db")

# Using the transaction_manager
with transaction_manager(connection) as transaction:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test (name) VALUES (?)", ("Alice",))
    # This would automatically commit unless an exception is raised