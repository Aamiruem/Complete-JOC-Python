# import random

# def generate_birthdays(n):
#     """Generate random birthdays for n people."""
#     birthdays = []
#     for _ in range(n):
#         # Generate a random day of the year (1-365)
#         birthday = random.randint(1, 365)
#         birthdays.append(birthday)
#     return birthdays

# def has_duplicates(lst):
#     """Check if there are any duplicate elements in the list."""
#     # If the length of the list is different from the length of the set, there are duplicates
#     return len(lst) != len(set(lst))

# def birthday_paradox_simulation(num_simulations, num_people):
#     """Simulate the birthday paradox."""
#     num_matches = 0
#     for _ in range(num_simulations):
#         birthdays = generate_birthdays(num_people)
#         if has_duplicates(birthdays):
#             num_matches += 1
#     probability = num_matches / num_simulations
#     return probability

# def main():
#     num_people = 23  # Number of people in the group
#     num_simulations = 10000  # Number of simulations
#     probability = birthday_paradox_simulation(num_simulations, num_people)
#     print(f"Probability of at least two people sharing a birthday in a group of {num_people}: {probability:.4f}")

# if __name__ == "__main__":
#     main()





import random
import datetime
birthday =[]
i = 0
while (i < 50):
    year = random.randint(1895, 2024)
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = 1
    else:
        leap = 0
    month = random.randint(1, 12)
    if(month == 2 and leap == 1):
        day = random.randint(1, 29)
    elif(month == 2 and leap == 0):
        day = random.randint(1, 28)
    elif(month == 7 or month == 8):
        day = random.randint(1, 31)
    elif(month%2!=0 and month <7):
        day = random.randint(1, 31)
    elif(month%2!=0 and month <7 and month < 12):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    birthday.append(day)
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday
    i = i+1
    birthday.append(day_of_year)
    
birthday.sort()
i = 0
while(i<50):
    print(birthday[i])
    i = i+1
