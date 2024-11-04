import random
from art import logo

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(arr):
    score = sum(arr)
    if score == 21 and len(arr) == 2:
        return 0
    if score > 21 and 11 in arr:
        arr.remove(11)
        arr.append(1)
    return sum(arr)

def compare(score1, score2):
    if score1 == score2:
        return 'It\'s a draw'
    elif score2 == 0:
        return 'You lose! Computer has a blackjack!'
    elif score1 == 0:
        return 'You win! You have a blackjack!'
    elif score1 > 21:
        return 'You lose. Your score is over 21.'
    elif score2 > 21:
        return 'You win! Computer score is over 21'
    elif score1 > score2:
        return 'You win!'
    else:
        return 'You lose!'

def play():
    print(logo)
    user = []
    comp = []
    comp_score = -1
    user_score = -1
    game = True
    for i in range(0,2):
        user.append(get_card())
        comp.append(get_card())
    while game:
        comp_score = calculate_score(comp)
        user_score = calculate_score(user)
        print(f'Your cards are: {user}. Your current score is {user_score}')
        print(f'Computer\'s first card is {comp[0]}')
        if user_score == 0:
            print('You win! You have a blackjack!')
            game = False
        elif comp_score == 0:
            print('You lose. Computer has a blackjack')
            game = False
        else:
            another_card = input('Would you like to draw another card? Type yes or no\n')
            if another_card.lower() == 'yes':
                user.append(get_card())
            elif another_card.lower() == 'no':
                game = False
            else:
                print('Invalid input')
                game = False

    while comp_score < 17 and comp_score != 0:
        comp.append(get_card())
        comp_score = calculate_score(comp)
    print(f'Let\'s reveal the cards!\nYour final score is {user_score}.\nComputer cards are: {comp}. Computer score is {comp_score}')
    print(compare(user_score, comp_score))

while input('Would you like to play a game of blackjack? Type y for yes and n for no') == 'y':
    print('\n' * 20)
    play()