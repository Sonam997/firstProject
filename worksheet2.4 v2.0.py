import os
os.system('clear')  
#  List of Departments
departments = [
    (1, "Computer Science"),
    (2, "Mathematics"),
    (3, "Computer Science"),
    (4, "Mathematics"),
    (5, "Physics"),
    (6, "Chemistry"),
    (7, "Biology"),
    (8, "Economics"),
    (9, "Economics"),
    (10, "Psychology"),
    (11, "History"),
    (12, "English"),
    (13, "Philosophy"),
    (14, "Mathematics"),
    (15, "Computer Science")
]
# Infinite loop until user enters 'quit' or '0'
while True:
    user_input = input("Enter a course ID (1-15), 'quit' to exit: ")
    if user_input.lower() == 'quit' or user_input == '0':
        print("Exiting program.")
        break
 # Search for department   
    course_id = int(user_input)
    found = False
    for id, dept in departments:
        if id == course_id:
            print(f"Course ID {course_id} is in the {dept} department.")
            found = True
            break
    
# Handle not found cases
    if not found:
        if course_id < 1 or course_id > 15:
            print("Course ID is out of range (1-15), try again.")
        else:
            print(f"The value {course_id} has been used to exit.")

# Multi-dimensional list storing course information
courses = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]

# Enhanced user interface with input validation
print("Course Information System")
print("Enter a course ID (1-15) to get details or 'quit' to exit")

while True:
    user_input = input("Enter course ID: ")
    if user_input.lower() == 'quit':
        print("Thank you for using the system. Goodbye!")
        break
    try:
        course_id = int(user_input)
    except ValueError:
        print("Please enter a valid number between 1-15 or 'quit'.")
        continue
    
# Search for course
    found = False
    for course in courses:
        if course[0] == course_id:
            print("Course Details")
            print(f"Course ID: {course[0]}")
            print(f"Name: {course[1]}")
            print(f"Department: {course[2]}")
            print(f"Prerequisites: {course[3]}")
            found = True
            break
    
# Handle not found cases
    if not found:
        if 1 <= course_id <= 15:
            print("Course ID found but no details available.")
        else:
            print("Invalid course ID. Please enter a number between 1-15.")
