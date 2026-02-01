"""
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar, and you gave shopkeeper 20 dollar.
Find out using python, how many dollars is the shopkeeper going to give you back?

3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
If tiles cost 500 dollars per square feet, how much will be the total cost to replace all tiles.
Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

4. Print binary representation of number 17
"""


# Area of the field
length = 92
width = 48.8

area = round((length * width), 2)

print(f'The Area of the field is {area} meters square')
print()


# Balance left after purchasing potato chips
packets_bought = 9
cost_per_packet = 1.49
paid_amount = 20

total_cost = packets_bought * cost_per_packet

balance = total_cost - paid_amount

if balance > 0:
    print(f"The balance is {balance} dollars")
elif balance == 0:
    print("There is no balance left")
else:
    print(f"You need to balance the shopkeeper with {-1 * balance} dollars")
print()


# Cost of replacing tiles
square_length = 5.5

bathroom_area = square_length ** 2

total_cost_of_tiles = bathroom_area * 500
print(f"The total cost of tiles is {total_cost_of_tiles} dollars")
print()


# Binary representation of number 17
number = 17

binary = bin(number)

print(f"The binary representation of number {number} is {binary[2:]}")
