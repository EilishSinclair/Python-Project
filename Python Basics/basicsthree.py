# Exercise One Weight Converter
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
    # converted = weight * 0.45
    # print(f"Your weight is {converted} kilos")
# else:
    # converted = weight / 0.45
    # print(f"Your weight is {converted} pounds")

# Exercise Two While Loops
#guess_count = 1
#while guess_count <= 5:
    #print ('*' * guess_count)
    #guess_count = guess_count + 1
#print("Completed")

# Exercise Three Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Yay you won!!!')
        break
else:
    print('Oh no try again another time!')