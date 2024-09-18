import sqlite3

class DatabaseManager:
    """A class to manage SQLite database connections and table creation."""

    def __init__(self, db_name):
        """Initialize the database manager with a database name."""
        self.db_name = db_name
        self.conn = None

    def create_connection(self):
        """Create a database connection."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to the database '{self.db_name}' successfully.")
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
        return self.conn

    def create_tables(self):
        """Create students and subjects tables."""
        if self.conn is None:
            print("Connection not established. Cannot create tables.")
            return

        try:
            cursor = self.conn.cursor()

            # Create the subjects table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS subjects (
                    subject_id INTEGER PRIMARY KEY,
                    subject_name TEXT NOT NULL
                )
            ''')

            # Create the students table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    roll_number INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    subject_id INTEGER,
                    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
                )
            ''')

            self.conn.commit()
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
