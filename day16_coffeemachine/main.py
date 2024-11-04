MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def proc_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

turn_on = True
while turn_on:
    user_input = input('What would you like to order? (espresso/latte/cappuccino): ')
    if user_input.lower() == 'cappuccino':
        if is_resource_sufficient(MENU['cappuccino']['ingredients']):
            given_money = proc_money()
            if is_transaction_successful(given_money, MENU['cappuccino']['cost']):
                make_coffee('cappuccino',MENU['cappuccino']['ingredients'])
    elif user_input.lower() == 'espresso':
        if is_resource_sufficient(MENU['espresso']['ingredients']):
            given_money = proc_money()
            if is_transaction_successful(given_money, MENU['espresso']['cost']):
                make_coffee('espresso', MENU['espresso']['ingredients'])
    elif user_input.lower() == 'latte':
        if is_resource_sufficient(MENU['latte']['ingredients']):
            given_money = proc_money()
            if is_transaction_successful(given_money, MENU['latte']['cost']):
                make_coffee('latte', MENU['latte']['ingredients'])
    elif user_input.lower() == 'report':
        print('Water: ', resources['water'], 'ml\nMilk: ', resources['milk'], 'ml\nCoffee: ', resources['coffee'], 'g\nMoney: $', profit)
    elif user_input.lower() == 'off':
        turn_on = False
    else:
        print('Invalid input.')
        turn_on = False