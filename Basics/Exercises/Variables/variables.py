"""
1) Create a variable called break and assign it a value 5.
See what happens and find out the reason behind the behavior that you see.

2) Create two variables. One to store your birth year and another one to store current year.
Now calculate your age using these two variables

3) Store your first, middle and last name in three different variables and then print your full name using these variables

4) Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue

"""


# Can't assign a value to break because a reserved keyword. Instead, you can add underscore to make it valid.
break_ = 5


# Calculate age
birth_year = 1995
current_year = 2026

age = current_year - birth_year
print(f"You are {age} years old")


# Print full name
first_name = "Jamaldeen"
middle_name = "Mohammed"
surname = ("Alhassan")

print(f"{first_name} {middle_name} {surname}")

