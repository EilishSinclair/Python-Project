# Exercise One Weight Converter
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilos")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds")

# Exercise Two While Loops
guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print("Completed")

# Exercise Three Exceptions
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

# Exercise Four Comments
# Use comments to explain Hows and Whys not Whats.
print("Travelling is great for the soul!")

# Exercise Five Classes
# Basic types in Python: Numbers, Strings and Booleans.
# Learnt about Lists, Dictionaries.
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

# Exercise Six Constructors
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, everyone my name is {self.name}")


daisy = Person("Daisy Robin")
daisy.talk()

christopher = Person("Christopher Robin")
christopher.talk()

# Exercise Seven Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Cat(Mammal):
    def be_cute(self):
        print("cute")

cat1 = Cat()
cat1.be_cute()