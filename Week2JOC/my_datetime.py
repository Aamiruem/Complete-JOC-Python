# # date and time

# import datetime

# # Get the current date and time
# current_datetime = datetime.datetime.now()
# print("Current date and time:", current_datetime)

# # Get the current date
# current_date = datetime.date.today()
# print("Current date:", current_date)

# # Get the current time
# current_time = datetime.datetime.now().time()
# print("Current time:", current_time)

# # Create a specific date
# specific_date = datetime.date(2022, 4, 18)
# print("Specific date:", specific_date)

# # Create a specific time
# specific_time = datetime.time(10, 30, 0)
# print("Specific time:", specific_time)

# # Combine date and time
# combined_datetime = datetime.datetime.combine(specific_date, specific_time)
# print("Combined datetime:", combined_datetime)

# # Formatting date and time
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_datetime)

# # Parsing date from string
# date_string = "2022-04-18"
# parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
# print("Parsed date:", parsed_date)




import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract individual components
current_date = current_datetime.date()
current_time = current_datetime.time()
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_minute = current_datetime.minute
current_second = current_datetime.second

# Print the extracted components
print("Current Date:", current_date)
print("Current Time:", current_time)
print("Day:", current_day)
print("Month:", current_month)
print("Year:", current_year)
print("Minute:", current_minute)
print("Second:", current_second)
