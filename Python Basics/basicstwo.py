# Exercise One Arithmetic Operations
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

# Exercise Two Operator Precedence
x = (10 + 3) * 2 ** 2
print(x)
# parenthesis
# exponentiation 2 ** 3
# multiplication or division
# addition or subtraction

# Exercise Three Math Functions
import math
print(math.floor(2.9))

# Exercise Four If Statements
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

# Exercise Five Logical Operators
has_good_background = True
has_good_references = True

if has_good_background and not has_good_references:
    print ("Eligible for adoption")

# Exercise Six Comparison Operators
name = "Bruce"

if len(name) < 3:
    print("Name has to be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")