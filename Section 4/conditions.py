name = input("What is your name?")
age = int(input(f"Hi {name}, how old are you?"))

if age >= 16 and age <= 65:
    print(f"Welcome to work {name}.")
else:
    print(f"{name}, you're not meant to be here, go home!")
