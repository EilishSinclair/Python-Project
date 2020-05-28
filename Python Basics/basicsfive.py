# Exercise One Comparison Operators
name = "Bruce"

if len(name) < 3:
    print("Name has to be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")


# Exercise Two Keyword Arguments
def greet_user(first_name, last_name):
    print(f'Hello and welcome {first_name} {last_name}')
    print(' To London, England!')

print("Start")
greet_user("Jan", last_name="Golding")
print("Finish")

# Exercise Three Return Statements
def square(number):
    print(number * number)

print(square(5))

# Exercise Four Creating A Reusable Function
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "🥰",
        ":(": "👧🏽"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

# Exercise Five Functions
def greet_user():
    print('Welcome to....')
    print('New York City!')
    print('Have a great trip.')


print("Start here")
greet_user()
print('Finish here')

# Exercise Six Parameters
def greet_user(first_name, last_name):
    print(f'Welcome {first_name} {last_name} to')
    print('New York City!')
    print('Have a great trip.')


print("Start here")
greet_user("Daisy", "Disney")
greet_user("Franklin", "Disney")
print('Finish here')