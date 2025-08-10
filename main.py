# Caitlyn Talbott
# 7.31.2025
# Final Project

# Build a Student Registration System

# Import necessary modules
import sqlite3  # Used to interact with SQLite databases
import json  # Used to read and write JSON files

# Set the database and JSON file names
DB_NAME = 'school.db'
JSON_FILE = 'data.json'


# SET UP THE DATABASE
# This function creates the tables if they don't already exist
def setup_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Create 'students' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        # Create 'courses' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL
            )
        ''')
        # Create 'registrations' table (links students to courses)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        ''')


# ADD A STUDENT
def add_student():
    name = input("Enter student name: ")
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO students (name) VALUES (?)", (name,))
    print("✅ Student added.")


# ADD A COURSE
def add_course():
    course_name = input("Enter course name: ")
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO courses (course_name) VALUES (?)", (course_name,))
    print("✅ Course added.")


# REGISTER A STUDENT FOR A COURSE
def register_student():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Get list of students
        students = cursor.execute("SELECT student_id, name FROM students").fetchall()
        if not students:
            print("⚠️ No students found.")
            return
        print("\nStudents:")
        for s in students:
            print(f"{s[0]}: {s[1]}")

        # Get list of courses
        courses = cursor.execute("SELECT course_id, course_name FROM courses").fetchall()
        if not courses:
            print("⚠️ No courses found.")
            return
        print("\nCourses:")
        for c in courses:
            print(f"{c[0]}: {c[1]}")

        # Ask user which student and course to link
        try:
            student_id = int(input("Enter student ID to register: "))
            course_id = int(input("Enter course ID to register to: "))
        except ValueError:
            print("❌ Invalid input.")
            return

        # Register the student
        cursor.execute("INSERT INTO registrations (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        print("✅ Student registered to course.")


# VIEW ALL STUDENTS
def view_students():
    with sqlite3.connect(DB_NAME) as conn:
        students = conn.execute("SELECT * FROM students").fetchall()
        print("\n👩‍🎓 Students:")
        for s in students:
            print(f"ID: {s[0]}, Name: {s[1]}")
        if not students:
            print("No students found.")


# VIEW ALL COURSES
def view_courses():
    with sqlite3.connect(DB_NAME) as conn:
        courses = conn.execute("SELECT * FROM courses").fetchall()
        print("\n📚 Courses:")
        for c in courses:
            print(f"ID: {c[0]}, Name: {c[1]}")
        if not courses:
            print("No courses found.")


# VIEW ALL REGISTRATIONS
def view_registrations():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT r.registration_id, s.name, c.course_name
            FROM registrations r
            JOIN students s ON r.student_id = s.student_id
            JOIN courses c ON r.course_id = c.course_id
        ''')
        registrations = cursor.fetchall()
        print("\n📝 Registrations:")
        for r in registrations:
            print(f"{r[0]}: {r[1]} → {r[2]}")
        if not registrations:
            print("No registrations found.")


# SEARCH FOR A STUDENT BY ID
def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))
    except ValueError:
        print("❌ Invalid input.")
        return
    with sqlite3.connect(DB_NAME) as conn:
        student = conn.execute("SELECT * FROM students WHERE student_id = ?", (student_id,)).fetchone()
        if student:
            print(f"✅ Found: ID {student[0]}, Name: {student[1]}")
        else:
            print("❌ Student not found.")


# EXPORT DATA TO JSON FILE
def export_to_json():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        data = {
            "students": cursor.execute("SELECT * FROM students").fetchall(),
            "courses": cursor.execute("SELECT * FROM courses").fetchall(),
            "registrations": cursor.execute("SELECT * FROM registrations").fetchall()
        }

    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print("📁 Data exported to", JSON_FILE)


# IMPORT DATA FROM JSON FILE
def import_from_json():
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)

        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Add students
            for student in data.get("students", []):
                cursor.execute("INSERT OR IGNORE INTO students (student_id, name) VALUES (?, ?)", student)

            # Add courses
            for course in data.get("courses", []):
                cursor.execute("INSERT OR IGNORE INTO courses (course_id, course_name) VALUES (?, ?)", course)

            # Add registrations
            for reg in data.get("registrations", []):
                cursor.execute(
                    "INSERT OR IGNORE INTO registrations (registration_id, student_id, course_id) VALUES (?, ?, ?)",
                    reg)

            conn.commit()
        print("✅ Data imported from", JSON_FILE)
    except FileNotFoundError:
        print("❌ JSON file not found.")


# DELETE STUDENT
def delete_student_by_name():
    name = input("Enter the name of the student to delete: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE name = ?", (name,))
        conn.commit()
    print(f"✅ All students named '{name}' have been deleted.")


# DELETE COURSE
def delete_course_by_name():
    name = input("Enter the name of the course to delete: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE course_name = ?", (name,))
        conn.commit()
    print(f"✅ All courses named '{name}' have been deleted.")


# MAIN MENU
def main():
    # Make sure database and tables are set up
    setup_database()

    while True:
        # Display menu options
        print("\n🎓 Student Registration System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student to Course")
        print("4. View Students")
        print("5. View Courses")
        print("6. View Registrations")
        print("7. Search Student by ID")
        print("8. Import from JSON")
        print("9. Export to JSON")
        print("10. Delete Student by Name")
        print("11. Delete Course by Name")
        print("0. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Run the selected function
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            register_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            view_courses()
        elif choice == '6':
            view_registrations()
        elif choice == '7':
            search_student()
        elif choice == '8':
            import_from_json()
        elif choice == '9':
            export_to_json()
        elif choice == '10':
            delete_student_by_name()
        elif choice == '11':
            delete_course_by_name()
        elif choice == '0':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter a number.")


# Only run the menu if the script is being run directly
if __name__ == "__main__":
    main()