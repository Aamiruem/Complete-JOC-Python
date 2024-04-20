from datetime import datetime

# Given dataset of birthdates (in format "YYYY-MM-DD")
birthdates = [
    "2000-01-01", "2000-02-02", "2000-03-03", "2000-04-04", "2000-05-05", "2000-06-06",
    "2000-07-07", "2000-08-08", "2000-09-09", "2000-10-10", "2000-11-11", "2000-12-12",
    # Add more birthdates here...
]

# Function to calculate the count of people born on a Tuesday
def count_tuesday_birthdays(birthdates):
    count = 0
    for birthdate in birthdates:
        # Convert the birthdate string to a datetime object
        birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
        # Check if the day of the week is Tuesday (weekday() returns 1 for Monday, 2 for Tuesday, and so on...)
        if birthdate_obj.weekday() == 1:
            count += 1
    return count

# Calculate the count of people born on a Tuesday
tuesday_count = count_tuesday_birthdays(birthdates)
print("Count of people born on a Tuesday:", tuesday_count)
