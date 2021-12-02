# parrot = "Norwegian Blue"

# letter = input("Enter charachters: ")

# if letter.casefold() in parrot.casefold():
#     print(f"'{letter}' is in '{parrot}'.")

# Challenge

name = input("What is your name? ")
age = int(input(f"Hello {name}, how old are you? "))

if 18 <= age <= 30:
    print(f"Welcome onboard the holiday train {name}, have fun!")
else:
    print(f"Sorry {name}, we cant allow you onboard the holiday train.")
