import sys
import random


def start():
    user = userChoice()
    computer = computerChoice()

    print('You choose: ', expand(user))
    print('Computer choose: ', expand(computer))
    print(compare(user, computer))


def compare(user, computer):
    cond1 = (user == 'r' and computer == 's')
    cond2 = (user == 'p' and computer == 'r')
    cond3 = (user == 's' and computer == 'p')
    if (user == computer):
        return 'Draw'
    if cond1 or cond2 or cond3:
        return 'You Won'
    else:
        return 'Computer Won'


def computerChoice():
    possible = possibleChoices()
    return possible[random.randint(0, 2)]


def userChoice():
    print("(R)ock")
    print("(P)aper")
    print("(S)cissors")
    print("(Q)uit")
    choice = input("What is your choice? ").lower()

    if choice == 'q':
        sys.exit(0)
    elif choice in ('r', 'p', 's'):
        return choice
    else:
        userChoice()


def possibleChoices():
    return ['r', 'p', 's']


def expand(choice):
    if choice == 'r':
        return 'Rock'
    if choice == 'p':
        return 'Paper'
    if choice == 's':
        return 'Scissors'


if (__name__ == "__main__"):
    start()
