import random
lowest, highest = 0, 10
answer = random.randint(lowest, highest)

print(f"Please guess a number between {lowest} and {highest}: ")
print(answer)  # TODO: Remove
guess = int(input())

while guess != answer:
    if guess == 0:
        break
    elif guess < answer:
        print("Too low, try again:")
    else:
        print("Too high, try again:")
    guess = int(input())

if guess == 0:
    print('You quit!')
else:
    print("Correct!")
