from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffem = CoffeeMaker()
menu = Menu()
moneypr = MoneyMachine()
turn_on = True
while turn_on:
    choice = input(f'What would you like? {menu.get_items()}: ')
    if choice.lower() == "off":
        turn_on = False
    elif choice.lower() == "report":
        CoffeeMaker.report(coffem)
        MoneyMachine.report(moneypr)
    elif choice == menu.find_drink(choice).name:
        order = menu.find_drink(choice)
        if coffem.is_resource_sufficient(order):
            if moneypr.make_payment(order.cost):
                coffem.make_coffee(order)

