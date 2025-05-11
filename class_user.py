"""
# Defining Student Profile
class User:
    def __init__(self, first_name, last_name, email=None, username=None, date_of_birth=None, location=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
    
    def describe_user(self):
        description = f"Name: {self.first_name} {self.last_name}"
        if self.email:
            description += f", Email: {self.email}"
        if self.username:
            description += f", Username: {self.username}"
        if self.date_of_birth:
            description += f", Date of Birth: {self.date_of_birth}"
        if self.location:
            description += f", Location: {self.location}"
        return description
    
    def greet_user(self):
        return f"Hello, {self.first_name}!"
# Creating instances of the User class
user1 = User("Alice", "Smith", email="alice@example.com", username="alice123", date_of_birth="1990-05-01", location="New York")
user2 = User("Bob", "Johnson", email="bob@example.com", username="bob456", date_of_birth="1985-09-10", location="London")
"""
"""
class User:
    def __init__(self, first_name, last_name, email=None, username=None, date_of_birth=None, location=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0  # Attribute to track login attempts
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
"""
"""
class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
    
    def describe_classroom(self):
        return f"Classroom: {self.classroom_name}, Location: {self.classroom_location}, Seats: {self.seats_in_class}"
    
    def checksize_classroom(self, enrolled_students):
        if enrolled_students > self.seats_in_class:
            return "Classroom is full, more seats are needed."
        else:
            return f"Classroom has enough seats for {enrolled_students} students."
"""
#"""
class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0  # Default value for students enrolled
        self.audit_log = []  # Audit log to track changes
    
    def set_number_enrolled(self, number):
        self.students_enrolled = number
        self.audit_log.append(f"Set number of students enrolled to {number}.")
    
    def update_number_enrolled(self, new_number):
        old_number = self.students_enrolled
        self.students_enrolled = new_number
        self.audit_log.append(f"Updated enrolled students from {old_number} to {new_number}.")
    
    def show_audit_log(self):
        return "\n".join(self.audit_log)
#"""   
class Equipment(Classroom):
    def __init__(self, classroom_name, classroom_location, seats_in_class, devices):
        super().__init__(classroom_name, classroom_location, seats_in_class)
        self.devices = devices  # List of devices in the classroom
    
    def display_devices(self):
        return f"Devices in the classroom: {', '.join(self.devices)}"