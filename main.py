print("Hello world")
#i see the hello world now (josh) i have the pusedo code fuffly done.

#pusedo code
##BEGIN

#1. Connect to SQLite database (school.db)
#2. If tables (students, course, registration) do not exist:
 #   CREATE students table (id, name, age, major)
 #   CREATE course table (id, name, credits)
 #   CREATE registration table (student_id, course_id)

#3. Load JSON file if exists:
#    FOR each student and course in JSON:
#        INSERT or UPDATE student into students table
 #       INSERT or UPDATE course into course table
#        INSERT or UPDATE into registration table

#4. LOOP until user exits:
#    DISPLAY menu:
#        1. Add new student
#        2. Add new course
#        3. View all students
#        4. View all courses
#        5. View all registrations
#        6. Search student by ID
#        7. Export data to JSON
 #       8. Exit

#    GET user choice

#    IF choice == 1:
#        PROMPT for student info
#        INSERT student

 #   ELSE IF choice == 2:
 #       PROMPT for course info
#        INSERT course

 #   ELSE IF choice == 3:
 #       SELECT * FROM students
 #       DISPLAY results

 #   ELSE IF choice == 4:
 #       SELECT * FROM course
 #       DISPLAY results

 #   ELSE IF choice == 5:
 #       SELECT * FROM registration
 #       DISPLAY results

 #   ELSE IF choice == 6:
 #       PROMPT for student ID
 #       SEARCH student by ID

 #   ELSE IF choice == 7:
 #       SELECT all tables' data
 #       EXPORT to JSON file

 #   ELSE IF choice == 8:
  #      BREAK

#END LOOP
#DISCONNECT from database

#END

# algorithm

#Start

#Connect to SQLite and create school.db

#Create tables:

#students(id PRIMARY KEY, name TEXT, age INTEGER, major TEXT)

#course(id PRIMARY KEY, name TEXT, credits INTEGER)

#registration(student_id, course_id, FOREIGN KEYS)

#If JSON data is available:

#Load and parse JSON

#Insert/update into tables accordingly

#3Show menu for user options

#Based on user selection, perform the respective database operation:

##Add students or courses

#View or search records

#Export to JSON

#Repeat until user exits

##Close database connection

#End
# flow chart
#Start Program
  #  ↓
#Read data from JSON file
  #  ↓
#Connect to school.db and create tables (if not exist)
  #  ↓
#Insert/Update JSON data into database
  ###  ↓
#Show Main Menu:
   # 1. Add Student
   # 2. Add Course
   # 3. View All Students
   # 4. View All Courses
   # 5. View All Registrations
    #6. Search Student by ID
   # 7. Export to JSON
   # 8. Exit
   # 9.help
   # ↓
#[User selects an option]
  #  ↓
#Perform selected action
  #  ↓
#Return to Main Menu? → Yes → (back to menu)
#                      ↓
#                     No
#                      ↓
#Export to JSON (if selected)
#    ↓
#Close DB and Exit Program





import sqlite3
import json


try:
    with open('regData.json', 'r') as file:
        data = json.load(file)
    print("Data loaded successfully.")
    print(data)
except:
    print("you suck at coding")
    quit()

while True:
    break

