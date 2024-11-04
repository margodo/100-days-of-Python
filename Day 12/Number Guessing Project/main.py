import random
from typing import final

from art import logo

def game():
    print(logo)
    print('Welcome to the game Guess The Number.\nRules are simple: computer generates a number from 1 to 100.\nIf you play easy mode, you have 10 attempts to guess.\nIf you play hard mode you have 5 attempts.\nAfter each attempt you will receive a hint whether your guess is too high or too low.')
    comp = random.randint(1,100)
    mode = input('Please choose the mode. Type \'easy\' or \'hard\'.\n')
    lives = 0
    if mode.lower() == 'easy':
        lives = 10
    elif mode.lower() == 'hard':
        lives = 5
    else:
        return 'Invalid input'
    while lives > 0:
        user = int(input('Try to guess a number:\n'))
        if user > comp:
            print('It is too high.')
            lives -= 1
        elif comp > user:
            print('It is too low.')
            lives -= 1
        elif user == comp:
            print('Great guess! You did great. You win.')
            return
        else:
            return 'Invalid input'
        print(f'Currently you have {lives} attempt(s)')
    if lives == 0:
        print(f'You did not manage to guess the number. The number was {comp}. Better luck next time!')
        return

game()
again = input('Would you like to play again? Type yes or no.\n')
if again == 'yes':
    print('\n' * 20)
    game()
elif again == 'no':
    print('Thank you for playing.')
else:
    print('Invalid entry.')