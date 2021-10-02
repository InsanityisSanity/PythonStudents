for i in range(1, 10):
    print("#{0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# adding spaces and formatting in the results

for i in range(1, 10):
    print("#{0:2} squared is {1:<3} and cubed is {2:^4}".format(
        i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))  # floating point format
# percision of 50 after the decimal point (max floaitng point in python is 53, anything after this will be a zero)
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.59f}".format(22/7))

# f-strings (not compatible with older versions of python below v3.4)

age = 24
print(f"You are {age} years old.")
print(type(age))
print()
pi = 22 / 7
print(f"Pi is approximately {22 / 7:12.50f}")
print(f"Pi is approximately {pi:12.50f}")
