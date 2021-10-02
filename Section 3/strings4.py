# Slicing

number = "5,433,555,743,247,149"

seperators = number[1::4]
print(seperators)

# Slicing backwards

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)
# note that -1 will not work for getting the first letter (a) to appear
backwards = letters[25::-1]
print(backwards)
