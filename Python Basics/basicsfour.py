# Exercise One Logical Operators
has_good_background = True
has_good_references = True

if has_good_background and not has_good_references:
    print("Eligible for adoption")

# Exercise Two Dictionaries
# Key Value Pairs
Name: DaisyFlower
Email: daisy@gmail.com
Phone: 0o1234
phone = input("Phone: ")
digits_mapping = {
 "1": "One",
 "2": "Two",
 "3": "Three",
 "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Exercise Three Emoji Converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "🥰",
    ":(": "✈️"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# Exercise Four Tuples
numbers = (1, 2, 3)
print(numbers[0])

# Exercise Five Unpacking
coordinates = [1, 2, 3,]
x, y, z = coordinates
print(z)

# Exercise Six List Methods
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)