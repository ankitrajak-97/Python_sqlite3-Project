import sqlite3
def generate_report(conn):
    
    try:
        cursor = conn.cursor()
        # SQL query to get the count of students for each subject
        query = '''
        SELECT 
            subjects.subject_name,
            COUNT(students.roll_number) AS student_count
        FROM 
            students
        JOIN 
            subjects ON students.subject_id = subjects.subject_id
        GROUP BY 
            subjects.subject_name;
        '''
        cursor.execute(query)
        
        # Fetch and print the results
        results = cursor.fetchall()
        print("Student Count vs Subject Report:")
        for row in results:
            print(f"Subject: {row[0]}, Student Count: {row[1]}")
            
    except sqlite3.Error as e:
        print(f"Error generating report: {e}")


def create_view_comp_sc(conn):
    try:
        cursor = conn.cursor()
        # SQL query to get the count of students for each subject
        query = '''
       create view comp_students as
       select * from students join subjects using(subject_id)
       where subject_name = 'Computer Science';
        '''
        cursor.execute(query)
        print("View 'computer_science_students' created successfully.")

        cursor.execute('''
            SELECT * FROM comp_students
        ''')
        
       
        
        
        
        rows = cursor.fetchall()

        if rows:
            print("\nAll Students Enrolled in Computer Science (from comp_students view):")
            print("---------------------------------------------------")
            for row in rows:
                roll_number, name, subject_id, subject_name = row
                print(f"Roll Number: {roll_number}, Name: {name}, Subject ID: {subject_id}, Subject: {subject_name}")
            print("---------------------------------------------------")
        else:
            print("No students found in Computer Science.")
    except sqlite3.Error as e:
        print(f"Error fetching data from view: {e}")        
