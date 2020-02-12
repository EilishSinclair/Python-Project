# Exercise One For Loops (Supermarket Cart)
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Exercise Two Nested Loops
#(x, y)
#(0, 0)
#(0, 1)
#(0, 2)
#(1, 0)
#(1, 1)
#(1, 2)
# for x in range(4):
    # for y in range(5):
        # print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

