import random
print("Guess The Number")

def guess_the_number():
    chances = 10
    low = 0
    high = 100

    number = random.randint(low, high)
    while True:
        guess = int(input(f'Guess a number between {low} and {high}: '))
        chances -= 1

        if guess == number:
            break

        elif guess < number:
            low = guess
            print('Too low')

        elif guess > number:
            high = guess
            print('Too high')


        print(f'You have {chances} guesses left.')

        if chances == 0:
            print('You lose!')
            quit()

    return number, chances

number, chances = guess_the_number()
print(f'You successfully guessed {number} with {10 - chances} attempts.')