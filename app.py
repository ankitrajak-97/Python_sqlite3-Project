import sqlite3
import json





# def create_connection(db_name):
#     """Create a database connection."""
#     conn = None
#     try:
#         conn = sqlite3.connect(db_name)
#         print(f"Connected to the database '{db_name}' successfully.")
#     except sqlite3.Error as e:
#         print(f"Error connecting to the database: {e}")
#     return conn

# def create_tables(conn):
#     """Create students and subjects tables."""
#     try:
#         cursor = conn.cursor()
#         # Create the subjects table
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS subjects (
#                 subject_id INTEGER PRIMARY KEY,
#                 subject_name TEXT NOT NULL
#             )
#         ''')
#         # Create the students table
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS students (
#                 roll_number INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 subject_id INTEGER,
#                 FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
#             )
#         ''')
#         conn.commit()
#         print("Tables created successfully.")
#     except sqlite3.Error as e:
#         print(f"Error creating tables: {e}")

def insert_subjects(conn, subjects):
    """Insert subjects data from JSON into the subjects table."""
    try:
        cursor = conn.cursor()
        for subject in subjects['subjects']:
            cursor.execute('''
                INSERT INTO subjects (subject_id, subject_name) VALUES (?, ?)
            ''', (subject['subject_id'], subject['subject_name']))
        conn.commit()
        print("Subjects inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting subjects: {e}")

def insert_students(conn, students):
    """Insert students data from JSON into the students table."""
    try:
        cursor = conn.cursor()
        for student in students['students']:
            cursor.execute('''
                INSERT INTO students (roll_number, name, subject_id) VALUES (?, ?, ?)
            ''', (student['roll_number'], student['name'], student['subject_id']))
        conn.commit()
        print("Students inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting students: {e}")

def print_all_rows(conn):
    """Print all rows from students and subjects tables."""
    try:
        cursor = conn.cursor()
        
        # Fetch and print all subjects
        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()
        print("(Subjects_id , subject_name)")
        for row in subjects:
            print(row)

        # Fetch and print all students
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print("\n(roll_number , name , subject_id)")
        for row in students:
            print(row)

    except sqlite3.Error as e:
        print(f"Error retrieving data: {e}")



def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(file_path)
        return data
    except Exception as e:
        print(f"Error loading JSON data from {file_path}: {e}")
        return None        

