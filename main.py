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
=======
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
>>>>>>> 2c35d65c72308741657b2a537cec0e4d46cf868e
