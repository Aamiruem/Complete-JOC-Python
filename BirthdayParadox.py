import random

def generate_birthday():
    # Generate a random integer between 1 and 365 (inclusive) representing a birthday
    return random.randint(1, 365)

# Simulate a group of people and record their birthdays
num_people = 23  # Number of people in the group
birthdays = [generate_birthday() for _ in range(num_people)]

# Check if there are any duplicate birthdays
if len(birthdays) != len(set(birthdays)):
    print("The Birthday Paradox is true!")
else:
    print("No shared birthdays found.")
