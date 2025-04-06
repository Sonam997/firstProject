# Question 1
# list of Courses (not alphabetical)
courses = ["Calculus I", "Data Structures and Algorithms", "Physics I", "Chemistry I", 
           "Biology I", "Microeconomics", "Introduction to Programming"]
# Sort Without Modifying Original list
sorted_list=sorted(courses)
print("The following courses are available for expression of interest if the students meet the prerequisites:", sorted_list)

# Question 2
# Replace a Course
original_course = "Chemistry I"
new_course = "Linear Algebra"
courses[courses.index(original_course)] = new_course
print("Course original_course has been withdrawn and replaced with new_course;", courses)

# Question 3
# Add new courses
# Insert at beginning
courses.insert(0, "Macroeconomics")
# Insert in middle
courses.insert(3, "Psychology I")
# Append at end
courses.append("History I")
print("Updated course list with new additions:", courses)

# Question 4
# Remove courses
unavailable = [courses.pop(0), courses.pop(2), courses.pop(3), courses.pop()]
print("The following courses are unavailable due to technical and room availability issues:", courses)
print("Remaining available courses:", courses)


