import random


print("welcome to mastermind")
print("attempt to guess the 4 digit code...")
print("You have 10 tries.")
print("The colors that could make up the code are: R G B Y W O")

colors = ['R', 'G', 'B', 'Y', 'W', 'O']

answer = random.choices(colors, k=4)
print(answer)


tries = 0
while True:
    guess = list(input("Guess a 4 digit code: ").split())
    tries += 1

    for i in guess:
        if i not in colors or len(guess) != 4:
            print("That's not a valid guess.")
            continue


    if guess == answer:
        break

    correct_position = 0
    incorrect_position = 0
    temp = answer
    for i in range(4):
        if guess[i] == answer[i]:
            correct_position += 1


        elif guess[i] in temp and guess[i] != answer[i]:
            incorrect_position += 1
            #temp.remove(guess[i])



    print(f'Correct position: {correct_position}  |  Incorrect position: {incorrect_position}')
    if tries == 10:
        print('you lost!')
        quit()

print(f'You guesssed the code in {tries} tries.')
