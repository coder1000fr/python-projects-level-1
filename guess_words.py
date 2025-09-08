import random

words_list = ['rainbow', 'car', 'computer', 'machine', 'house', 'victory']

word = random.choice(words_list)
guess_list = ["_" for i in range(len(word))]

attempts = 10

while True:
    print(' '.join(guess_list))

    guess = input(">> ")
    attempts -= 1

    if guess == word:
        break

    elif guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                guess_list[i] = guess

    elif guess not in word:
        print(f'{guess} is not in the word')


    if attempts == 0:
        print("You lost!")
        quit()

print(f'You guess the word: {word} , in {10 - attempts} attempts')