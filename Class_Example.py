""""
#Example:
import os
# Clear terminal screen
os.system('clear')  
toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in toppings:
    print("Adding mushrooms.")
if 'extra cheese' in toppings:
    print("Adding extra cheese.")

#This checks if the toppings list is empty before proceeding​​
    toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
"""
"""
#This code checks if each requested topping is available

available_toppings = ['mushrooms', 'olives', 'green peppers', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries']
for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}.")
"""
