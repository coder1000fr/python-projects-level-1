import random

def guess_the_number():
    chances = 10
    low = 0
    high = 100
    print(f'Choose a number between {low} and {high}')

    while True:
        computer = random.randint(low, high)
        chances -= 1
        answer = input(f'Computer guessed {computer}, is it correct(c), low(l) or high(h)? ')
        if answer == 'c':
            break
        elif answer == 'l':
            low = computer + 1
        elif answer == 'h':
            high = computer - 1

        if chances == 0:
            print('Computer lost!')
            quit()

    return computer, chances

number, chance = guess_the_number()
print(f'Computer successfuly guessed {number} with {10 - chance} attempts.')