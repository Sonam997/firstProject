"""
class Dog:
   
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")
"""
#"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
#"""
#"""
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
#"""
"""
# Parent class
class Person:
    def speak(self):
        print("The person can speak")

# Child class (inherits from Person)
class Kid(Person):
    def play(self):
        print("The kids play with toys")
"""


