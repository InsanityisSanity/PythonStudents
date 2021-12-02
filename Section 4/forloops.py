# parrot = "Norwegian Blue"

# for charachter in parrot:
#     print(charachter)

number = "9,432 565+246.775;332"
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(
    char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
