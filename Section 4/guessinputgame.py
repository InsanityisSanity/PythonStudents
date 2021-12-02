answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())


# if guess < answer:
#     print("Too low, guess again.")
#     guess = int(input())
#     if guess == answer:
#         print("CORRECT, you got it on the second try!")
#     else:
#         print("Wrong, you lose!")
# elif guess > answer:
#     print("Too high, guess again.")
#     guess = int(input())
#     if guess == answer:
#         print("CORRECT, you got it on the second try!")
#     else:
#         print("Wrong, you lose!")
# else:
#     print("CORRECT!")

# if guess != answer:
#     if guess < answer:
#         print("Too low, try again:")
#     else:
#         print("Too high, try again:")
#     guess = int(input())
#     if guess == answer:
#         print("Correct!")
#     else:
#         print("Nope!")
# else:
#     print("Correct, you got it first time!")

if guess == answer:
    print("Correct, you got it first time!")
else:
    if guess < answer:
        print("Too low, try again:")
    else:
        print("Too high, try again:")
    guess = int(input())
    if guess == answer:
        print("Correct!")
    else:
        print("Nope!")
