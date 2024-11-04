from turtledemo.penrose import start

import art
import game_data
import random

def get_person_info(person):
    person_info = f'{person['name']}. {person['description']}. Is from {person['country']}.'
    return person_info

def get_person():
    person = random.choice(game_data.data)
    return person

def compare_fol(p1,p2):
    if p1['follower_count'] >= p2['follower_count']:
        return 'A'
    else:
        return 'B'

def game():
    print(art.logo)
    game_flow = True
    score = 0
    person2 = get_person()
    while game_flow:
        person1 = person2
        person2 = get_person()
        print(f'Compare A: {get_person_info(person1)}\n{art.vs}\nAgainst B: {get_person_info(person2)}')
        while person1 == person2:
            person2 = get_person()
        user_input = input('Who has more followers? Type \'A\' or \'B\'.\n')
        if user_input.upper() == compare_fol(person1, person2):
            score += 1
            print(f'Good job! You are right. Current score is {score}')
        elif user_input.upper() != compare_fol(person1, person2):
            print(f'Oh no you guessed it wrong. Game over. Your current score is {score} or you have entered invalid entry.')
            game_flow = False

game()
start_over = input('Would you like to start over? Type y or n.\n')
start_over_again = True
while start_over_again:
    if start_over.lower() == 'y':
        game()
    elif start_over.lower() == 'n':
        print('Thank you for playing!')
        start_over_again = False
    else:
        print('Invalid')
        start_over_again = False