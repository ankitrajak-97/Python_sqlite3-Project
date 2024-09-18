
import os
from app import insert_students,insert_subjects,print_all_rows,load_json
from reports import generate_report,create_view_comp_sc
from db_manager import DatabaseManager
def main():
     # Define the folder where JSON files are stored
    data_folder = 'data'

     # Load JSON data from files in the 'data' folder
    subjects_data = load_json(os.path.join(data_folder, 'subjects.json'))
    students_data = load_json(os.path.join(data_folder, 'students.json'))


     # Ensure the data was loaded successfully
    if subjects_data is None or students_data is None:
        print("Failed to load JSON data.")
        return
    
    # Create a database connection
    db_manager = DatabaseManager('students_db.db')
    conn = db_manager.create_connection()
    
    
    
    # Create tables if connection is established
    if conn is not None:
        db_manager.create_tables()
        
        insert_subjects(conn, subjects_data)
        insert_students(conn, students_data)
        #print_all_rows(conn)
        generate_report(conn)
        create_view_comp_sc(conn)
    else:
        print("Failed to create the database connection.")
    
    # Close the database connection
    if conn:
        conn.close()

if __name__ == "__main__":
    main()