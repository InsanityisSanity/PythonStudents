# Slicing

number = "5,433,555,743,247,149"

seperators = number[1::4]
print(seperators)

# Slicing backwards
#          12345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)
# note that -1 will not work for getting the first letter (a) to appear
backwards = letters[25::-1]
print(backwards)

# Lesson Excercise Start

# Print letters qpo
print(letters[16:13:-1])
# Print edcba
print(letters[4::-1])
# Print last 8 charachters in reverse order
print(letters[25:17:-1])

# Lesson Excercise End

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
