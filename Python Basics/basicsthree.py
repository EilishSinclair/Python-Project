# Exercise One Math Functions:
import math
print(math.floor(2.9))

# Exercise Two If Statements:
is_happy = False
is_excited = False

if is_happy:
    print("Glad your happy today")
    print("Be happy everyday")
elif is_excited:
    print("Have excitement")
    print("Make sure to become excited")
else:
    print("It's a beautiful day today!")

print("Remember to be happy tomorrow ")

# Exercise Three For Loops (Supermarket Cart)
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Exercise Four Nested Loops
 # (x, y)
 # (0, 0)
 # (0, 1)
 # (0, 2)
 # (1, 0)
 # (1, 1)
 # (1, 2)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
       output += 'x'
    print(output)

# Exercise Five Lists
numbers = [ 3, 6, 10, 2, 8, 4,]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# Exercise Six Two D Lists
matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)