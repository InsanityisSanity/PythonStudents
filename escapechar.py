splitString = 'This string has been \nsplit in to\ndifferent lines in order\nto test this\nfunctionality.'
print(splitString)
print()
print("I am now\tgoing to test\tthe tabbed\tfeature.")
print("""Using 3 brackets means I can use any feature inside that i want, for example, lots of '' and ' and " and "" because its cool.""")
print("""This has
been split
over several
lines.""")
print("""This has \
been split \
over several \
lines but the backslashes cancel it out.""")

# Bypassing escape charachters in strings

print("C:\\Users\\tuna\\notes.exe")  # Using double backslashes
print(r"C:\Users\tuna\notes.exe")  # Using r (raw format)

age = 24
name = 'Pouya'
print(name + ' is ' + str(age))
print(type(age))
print(type(name))
