import random

employees = ('Diego', 'Pouya', 'Bruno', 'Lukasz', 'Lina',
             'Larissa', 'Gabriela', 'Ed', 'Tyrell')
total_employees = len(employees)
total_on_site = random.randint(1, total_employees)
employees_on_site = ''
on_site_count = total_on_site

while on_site_count != 0:
    save = employees[random.randint(0, total_employees - 1)]
    if save not in employees_on_site:
        employees_on_site = employees_on_site + save
        on_site_count -= 1

code = random.randint(1, 33)
# TODO: Delete after production
print(f'Code: {code}. Employees on site: {total_on_site}')
name = str(input('Please enter your name: '))
age = int(input(f"Hello {name}, how old are you? "))

if age < 18:
    print(
        f"Sorry {name}, you're not old enough to use this application!\nGoodbye.")
    exit()
else:
    attempts = 5
    print(
        f"Welcome {name}. You must now guess the correct Secret Code!")

    while attempts > 0:
        guess = int(input(
            f'What is the correct code? You have {attempts} attempts left: '))

        if guess == code:
            attempts = -1
            print('Well done, you got it.')
        else:
            attempts -= 1
            print('Sorry, you guessed incorrectly.')
            if guess < code:
                print('Try guessing higher!')
            else:
                print('Try guessing lower!')

        if attempts == 0:
            print('You are out of guesses!\nGoodbye.')
            exit()
        elif attempts == -1:
            continue

print()
print('-' * 33)
print()
print(
    f'Welcome to the application, there are {total_employees} employed in the company and currently {total_on_site} working on site.\n\n')
print('The useless mouth breathers working on site today are:\n\n')
print(*employees, sep="\n")
