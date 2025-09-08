import random
import emoji

choices = ["rock", "paper", "scissors"]

def win(user, computer):
    status = 'draw'
    if user == 'r':
        if computer == 'scissors':
            status = 'win'
        elif computer == 'paper':
            status = 'lose'
    elif user == 'p':
        if computer == 'rock':
            status = 'win'
        elif computer == 'scissors':
            status = 'lose'
    elif user == 's':
        if computer == 'paper':
            status = 'win'
        elif computer == 'rock':
            status = 'lose'
    return status

def show(choice):
    if choice in ("rock", 'r'):
        return emoji.emojize(':raised_fist:')
    elif choice in ("paper", 'p'):
        return emoji.emojize(':raised_hand:')
    elif choice in ("scissors", 's'):
        return emoji.emojize(':victory_hand:')


def rock_paper_scissors():
    user = input("Rock paper scissors: ")
    print(f'user >> {show(user)}')
    computer = random.choice(choices)
    print(f'computer >> {show(computer)}')

    status = win(user, computer)
    if status == 'win':
        print('You won!')
    elif status == 'lose':
        print('You lost!')
    else:
        print('It\'s a tie!')

rock_paper_scissors()

while True:
    print("Do you want to play again?")
    choice = input('y / n? ')
    if choice == 'y':
        rock_paper_scissors()
    elif choice == 'n':
        break