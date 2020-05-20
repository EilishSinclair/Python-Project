# Exercise One Keyword Arguments
def greet_user(first_name, last_name):
    print(f'Hello and welcome {first_name} {last_name}')
    print(' To London, England!')

print("Start")
greet_user("Jan", last_name="Golding")
print("Finish")

# Exercise Two Return Statements
def square(number):
    print(number * number)

print(square(5))

# Exercise Three Creating A Reusable Function
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

# Exercise Four Exceptions
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

# Exercise Five Comments
# Use comments to explain Hows and Whys not Whats.
print("Travelling is great for the soul!")

# Exercise Six Classes
