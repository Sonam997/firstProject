# A. List of Departments
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
    
# Exit condition
    if user_input.lower() == 'quit' or user_input == '0':
        print("Exiting program.")
        break
    
# Input validation
    #try:
        #course_id = int(user_input)
    #except ValueError:
        #print("Please enter a valid number or 'quit'.")
        #continue
# Search for department
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
