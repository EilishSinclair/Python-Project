 # Exercise One For Loops (Supermarket Cart)
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Exercise Two Nested Loops
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

# Exercise Three Lists
numbers = [ 3, 6, 10, 2, 8, 4,]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# Exercise Four Two D Lists
matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

# Exercise Five List Methods
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Exercise Four Tuples
# numbers = (1, 2, 3)
# print(numbers[0])

# Exercise Five Unpacking
# coordinates = [1, 2, 3,]
# x, y, z = coordinates
# print(z)

# Exercise Six Dictionaries
# Key Value Pairs
# Name: Daisy Flower
# Email: daisy@gmail.com
# Phone: 01234
# phone = input("Phone: ")
# digits_mapping = {
 #"1": "One",
 #"2": "Two",
 #"3": "Three",
 #"4": "Four"
#}
#output = ""
#for ch in phone:
    #output += digits_mapping.get(ch, "!") + " "
#print(output)

# Exercise Seven Emoji Converter
# message = input(">")
# words = message.split(' ')
# emojis = {
    # ":/": "🥰",
    # ":(": "🏆️",
    # ":)": "👩‍🦽🧑🏻‍🦽🧑🏼‍🦽🚶🏽‍♀️🧑🏽‍🦯🏃🏼‍♀️🧑🏾‍🦼🕴🏽👩🏻‍🦽🧑🏿‍🦼"
# }
# output = ""
# for word in words:
    # output += emojis.get(word, word) + " "
# print(output)

# Exercise Eight Functions
# def greet_user():
    # print('How are you?')
    # print('How is your day going?')


# print("Start")
# greet_user()
# print("Finish")

# Exercise Nine Parameters
def greet_user(name):