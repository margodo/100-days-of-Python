# TODO-1: Ask the user for input
from Scripts.activate_this import bin_dir
def find(bid_dict):
    winner = ''
    highest = 0
    for bid in bid_dict:
        bid_amount = bid_dict[bid]
        if bid_amount  > highest:
            highest = bid_amount
            winner = bid
    print(f'The winner is {winner}. The highest bid is {highest}')
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
new_bid = True
auction = {}
while new_bid:
    name = input('Hi! Welcome to auction. What is your name?')
    bid = int(input('Pleasure to meet you. How much would you like to bid in US $: '))
    auction[name] = bid
    new_user = input('Would you like to enter new user? Type y for yes and n for n.')
    if new_user.lower() == 'n':
        new_bid = False
        find(auction)
    elif new_user.lower() == 'y':
        print('\n' * 20)
        continue
    else:
        print('Incorrect input')
# TODO-4: Compare bids in dictionary



