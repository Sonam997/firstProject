# Question 1
# list of courses
courses = ["Introduction to Programming","Calculus I", "Data Structures and Algorithms", 
           "Linear Algebra", "Physics I", "Chemistry I", "Biology I", "Microeconomics", 
           "Macroeconomics", "Psychology I", "History I", "English Composition I", 
           "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
# Print original list
print("Original list:", courses)
# Question 2
# Sorted list in alphabetical Order
sorted_list=sorted(courses)
print("Sorted List in Alphabetical Order:", sorted_list)
# Sorted List in Reverse Order
sorted_list1=sorted(courses, reverse=True)
print("Sorted List in Reverse Alphabetical Order:", sorted_list1)
# Question 3
# Reverse Order
courses.reverse()
print("Reverse Order:", courses)
# Reverse Back list
courses.reverse()
print("Reverse Back List:", courses)
# Question 4
# List Sort in Alphabetical Order
courses.sort()
print("Sort List in Alphabetical Order:", courses)
# List Sort in Reverse Alphabetical Order
courses.sort(reverse=True)
print("Sort List in Reverse Alphabetical Order:", courses)


