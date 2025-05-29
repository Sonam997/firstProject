"""
#Excersise 1
import os
# Clearing Screen
os.system("clear")
class PythonLearning:
    def __init__(self, filename):
        self.filename = filename

    def write_summary(self):
        content = [
            "Python is a powerful high-level programming language.",
            "It supports OOP, functional programming, and scripting.",
            "Error handling is done using try, except blocks."
        ]
        try:
            with open(self.filename, 'w') as file:
                file.write('\n'.join(content))
        except Exception as e:
            print(f"Error writing file: {e}")

    def read_entire_file(self):
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except Exception as e:
            print(f"Error reading file: {e}")

    def read_line_by_line(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
        except Exception as e:
            print(f"Error reading file: {e}")

app = PythonLearning("summary.txt")
app.write_summary()
app.read_entire_file()
app.read_line_by_line()
"""
"""
#Excersise 2
import os
# Clearing Screen
os.system("clear")
# Create file
with open("learning_students.txt", "w") as file:
    file.write("Every learner must complete their assignments on time. 
A good learner always seeks to learn more. 
Learners are the future leaders.")

# Replace and print
with open("learning_students.txt", "r") as file:
    for line in file:
        print(line.replace("learner", "student").replace("Learners", "Students"))
"""
"""
#Excersise 3
import os
# Clearing Screen
os.system("clear")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum = {num1 + num2}")
except ValueError:
    print("Error: Please enter valid numbers only!")
"""
"""
#Excersise 4
import os
# Clearing Screen
os.system("clear")
def read_files():
    try:
        with open("students_c1.txt", "r") as file1:
            print("File 1:\n", file1.read())
    except FileNotFoundError:
        print("students_c1.txt not found.")

    try:
        with open("students_c2.txt", "r") as file2:
            print("File 2:\n", file2.read())
    except FileNotFoundError:
        print("students_c2.txt not found.")

read_files()
"""
"""
import json
#Excersise 5
import os
# Clearing Screen
os.system("clear")

# Save
favourite = input("Enter your favourite number: ")
with open("favourite_number.json", "w") as f:
    json.dump(favourite, f)

# Read
with open("favourite_number.json", "r") as f:
    fav = json.load(f)
    print(f"Your favourite number is {fav}")
"""
"""
import json
#Excersise 6
import os
# Clearing Screen
os.system("clear")
# Collect and Save
student_id = input("Enter student ID: ")
user_data = {"StudentID": student_id}
with open("user_profile.txt", "w") as f:
    json.dump(user_data, f)

# Load and Update
with open("user_profile.txt", "r") as f:
    data = json.load(f)

dob = input("Enter date of birth: ")
email = input("Enter email: ")
data["DOB"] = dob
data["Email"] = email

with open("user_profile.txt", "w") as f:
    json.dump(data, f)

# Display
print(f"Student Info: {data}")
"""
"""
#Excersise 7
import os
# Clearing Screen
os.system("clear")
def get_student_info():
    messages = []
    try:
        with open("students.csv", "r") as file:
            for line in file:
                parts = line.strip().split()
                student_id, first, last = parts[0], parts[1], parts[2]
                messages.append(f"Hello {first} {last}, your student ID is {student_id}.")
        return messages
    except FileNotFoundError:
        return ["students.csv not found."]
"""
"""
#Excersise 8
import os
# Clearing Screen
os.system("clear")
from student_functions import get_student_info

def test_get_student_info():
    expected = [
        "Hello Alice Smith, your student ID is 1001.",
        "Hello Bob Johnson, your student ID is 1002."
    ]
    output = get_student_info()
    assert all(msg in output for msg in expected)

test_get_student_info()

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

# Test
emp = Employee("John", "Doe", 50000)
emp.give_raise()
print(emp.salary)  # Should print 55000
emp.give_raise(10000)
print(emp.salary)  # Should print 65000
"""
"""
import os
# Clearing Screen
os.system("clear")
from employee import Employee

def test_give_default_raise():
    emp = Employee("A", "B", 40000)
    emp.give_raise()
    assert emp.salary == 45000

def test_give_custom_raise():
    emp = Employee("C", "D", 40000)
    emp.give_raise(7000)
    assert emp.salary == 47000

test_give_default_raise()
test_give_custom_raise()
"""