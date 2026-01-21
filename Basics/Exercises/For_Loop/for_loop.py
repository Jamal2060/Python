"""
=================
Question 1
=================
"""

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
counter = 0  #Initializing count to store the number of times head appeared

for i in range(0, len(result)):   #looping through the results
    if result[i] == "heads":      #Checking if the value of the index is equal to heads
        counter += 1              # Increase the counter if is equal to heads

print("Heads appeared " + str(counter) + " times")  #Prints the outcome



"""
=================
Question 2
=================
"""

for i in range(1, 11):    #Looping through 1 to 10. Remember the end argument is not inclusive
    if i % 2 == 1:        #checking if odd number
        square = i ** 2   #squaring the odd number
        print(f"The square of {i} is: {square}")    #printing the outcome


"""
=================
Question 3
=================
"""

expense_list = [2340, 2500, 2100, 3100, 2980]
month = ["January", "February", "March", "April", "May"]

expense = int(input("Enter the expense: "))

for i in range(0, len(expense_list)):             #Looping through the list of expenses
    if expense_list[i] == expense:                # if the inputted expense is found in the expense list
        print(f"The expense of {expense} happened in: {month[i]}")
        break

else:                                             # If the inputted expense is not found in the expense list
    print(f"The expense of {expense} did not happened in any of the months")


"""
=================
Question 4
=================
"""

for i in range(1, 6):
    #Pring the number of KM and asking if their tired or not
    print(f"{i}KM Completed")
    tired = input("Are you tired? (Y/N): ")

    #To check if their answer is yes or no
    if tired.upper() == "Y":
        print("You didn't finish the race")
        break
    if tired.upper() == "N":
        continue        #This is to loop through until the range is exhausted

else:
    print("Congratulations! You finished the race")



"""
=================
Question 5
=================
"""

for i in range(1, 6):
    print(f"{"*" * i}")     #Multiplying the string "*" by the value of the index



