#         01234567890123
parrot = "Norwegian Blue"

# The last charachter when slicing does not appear in the final result (up to but not including)
print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:5])
print(parrot[:5])  # The zero is not needed if starting from index zero

print()

print(parrot[10:14])
# The last index number is not needed if ending slice at the last index
print(parrot[10:])
print(parrot[:5] + parrot[5:])
# This method is not useful when working with strings, we will find out later what it can be used for
print(parrot[:])

print()

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[5:11])

print()

print(parrot[0:9:2])
print(parrot[0:9:3])
