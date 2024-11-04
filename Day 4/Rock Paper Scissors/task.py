import random
print('Hi! Let\'s play rock-paper-scissors.')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
comp = random.randint(0,2)
user_choice = int(input('To start please enter 0 for rock; 1 for paper; 2 for scissors'))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number.")
elif user_choice == comp:
    print(f"Computer chose {game[comp]}\nYou chose {game[user_choice]}")
    print('It\'s a draw')
elif user_choice == 0 and comp == 2:
    print(f"Computer chose {game[comp]}\nYou chose {game[user_choice]}")
    print("You win!")
elif comp == 0 and user_choice == 2:
    print(f"Computer chose {game[comp]}\nYou chose {game[user_choice]}")
    print("You lose! Better luck next time.")
elif comp > user_choice:
    print(f"Computer chose {game[comp]}\nYou chose {game[user_choice]}")
    print("You lose! Better luck next time.")
elif user_choice > comp:
    print(f"Computer chose {game[comp]}\nYou chose {game[user_choice]}")
    print("You win!")
