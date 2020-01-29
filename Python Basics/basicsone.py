# Exercise One Variables (Integers):
# The number Ten is an integer.
price = 10

# Exercise Two Variables (Floats):
# The number Four Point Nine as a floating point number or floats for short.
rating = 4.9

# Exercise Three Variables (Strings):
# The Cat is a string.
name = 'Cat'

# Exercise Four Variables (Booleans):
# The True and False are Booleans. When defining variables should always use lower case letters.
is_published = True
is_published = False

print(price)

# Exercise Five Receiving Input:
full_name = 'John Smith'
age = 20
is_new = True

# Exercise Six Python Cheat Sheet:
name = input('Who are you? ')
favourite_animal = input('Whats your favourite animal? ')
favourite_travel = input('Where is your favourite place to travel too? ')
message = input('I would like to write ')
print(name + ' likes ' + favourite_animal + ' and loves ' + favourite_travel + ' Thank you so much for watching! ')

#Exercise Seven Type Conversion:
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Exercise Eight Strings:
# You need to use double quites when using an apostrophe, negative one is the index for the last character.
course = 'How to become a star'
another = course[1:5]

# Exercise Nine Formatted strings:
# A formatted string is f'' and example: f'{first_name} [{last_name}] is funny'
dog_name = 'Snow White'
dog_interest = 'Sleeping'
message = dog_name + ' [' + dog_interest + '] loves it! '
msg = f'{dog_name} [{dog_interest}] loves it!'
print(msg)