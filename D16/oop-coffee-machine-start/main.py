from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

contd = True
while contd:
    ch = input(f"What would you like? {menu.get_items()}: ")
    if ch == "report":
        coffeemaker.report()
        moneymachine.report()
    elif ch == "off":
        contd = False
    else:
        drink = menu.find_drink(ch)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
