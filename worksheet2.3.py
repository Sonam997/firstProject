# Question 1
# Create list of tuples
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]

# Create empty list 
course_names = []
for course_id, name in course_tuples:
    course_names.append(name)

# Print course information
print("Course Information:")
for i, name in enumerate(course_names, 1):
    print(f"{i}. {name}")