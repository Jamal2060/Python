"""
==================
Question 1
==================
"""

expenses = [2200, 2350, 2600, 2130, 2190]
month = ["January", "February", "March", "April", "May"]

# 1. In Feb, how many dollars you spent extra compare to January?
print("\n Question 1.a \n")

extra_expense = expenses[1] - expenses[0]
print(f"The amount of money spent extra in February compared to January is: {extra_expense} dollars")

# 2. Find out your total expense in first quarter (first three months) of the year.
print("\n Question 1.b \n")

first_quarter = expenses[0] + expenses[1] + expenses[2]
print(f"The total expenses in the first quarter of the year is: {first_quarter} dollars")

# 3. Find out if you spent exactly 2000 dollars in any month
print("\n Question 1.c \n")

for i in range(len(expenses)):
    if expenses[i] == 2000:
        print(f"You have spent exactly 2000 dollars in {month[i]}")
        break
else:
    print(f"You have not spent exactly 2000 dollars in any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("\n Question 1.d \n")

expenses.append(1890)
print(f"List after adding June expenses: {expenses}")

# 5. You returned an item that you bought in a month of April and
#    got a refund of 200$. Make a correction to your monthly expense list
#    based on this
print("\n Question 1.e \n")

refund = expenses[3] - 200
expenses[3] = refund
print(f"List after refund: {expenses}")


"""
==================
Question 2
==================
"""
print("\n Question 2.a \n")

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(f"Length of the list is: {len(heros)}")


# 2. Add 'black panther' at the end of this list
print("\n Question 2.b \n")

heros.append("black panther")
print(f"List after adding black panther: {heros}")


# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
print("\n Question 2.c \n")

heros.remove("black panther")
heros.insert(3, "black panther")
print(f"List after changing black panther position: {heros}")


# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
print("\n Question 2.d \n")

heros[1:3] = ["doctor strange"]
print(f"List after replacing thor and hulk: {heros}")


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print("\n Question 2.e \n")

heros.sort()
print(f"List after sort: {heros}")



