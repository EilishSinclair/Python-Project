#Exercise One Type Conversion:
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Exercise Two Strings:
# You need to use double quites when using an apostrophe, negative one is the index for the last character.
course = 'How to become a star'
another = course[1:5]

# Exercise Three Formatted strings:
# A formatted string is f'' and example: f'{first_name} [{last_name}] is funny'
dog_name = 'Snow White'
dog_interest = 'Sleeping'
message = dog_name + ' [' + dog_interest + '] loves it! '
msg = f'{dog_name} [{dog_interest}] loves it!'
print(msg)

# Exercise Four String Methods:
course = 'How to become stars'
# len()
# course.upper()
# course.lower()
# course.title()
# course.find()
# course.replace()
# '....' in course

# Exercise Five Arithmetic Operations:
# Adding
print(10 + 3)
# Subtracting
print(10 - 3)
# Multiplication
print(10 * 3)
# Division One Way (Floating point number)
print(10 / 3)
# Division The Other way (An Integer)
print(10 // 3)
# Module list (Returns remainder of the division)
print(10 % 3)
# Exponent (Is the power)
print(10 ** 3)
# Augmented assignment operator.
x = 10
x += 3
print(x)

# Exercise Six Operator Precedence:
x = (10 + 3) * 2 ** 2
print(x)
# parenthesis
# exponentiation 2 ** 3
# multiplication or division
# addition or subtraction