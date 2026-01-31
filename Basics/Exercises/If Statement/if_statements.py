"""
1. Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

i) Write a program that asks user to enter a city name and it should tell which country the city belongs to
ii) Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai
and dhaka it should print "They don't belong to same country"

"""

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# i. User enters a city name to find out which country it belongs to
city_name = input("Please enter a city name: ")

if city_name.lower() in india:
    print("The city " + city_name + " is in India")
elif city_name.lower() in pakistan:
    print("The city " + city_name + " is in Pakistan")
elif city_name.lower() in bangladesh:
    print("The city " + city_name + " is in Bangladesh")
else:
    print("The city " + city_name + " that's not exit")


# ii. User enters two city names to find out if it belongs to the same country.
city1 = input("Please enter the first city name: ")
city2 = input("Please enter the second city name: ")

if (city1 in india) and (city2 in india):
    print("Both cities are in India")
elif (city1 in pakistan) and (city2 in pakistan):
    print("Both cities are in Pakistan")
elif (city1 in bangladesh) and (city2 in bangladesh):
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")



"""
2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.

i) Ask user to enter his fasting sugar level
ii) If it is below 80 then print that sugar is low
iii) If it is above 100 then print that it is high otherwise print that it is normal

"""

sugar_level = float(input("Please enter your sugar level: "))

if 80 <= sugar_level <= 100:
    print("Your sugar level is normal")
elif sugar_level < 80:
    print("Your sugar level is low")
else:
    print("Your sugar level is high")