from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# is_on = True
#
# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
#
# while is_on:
#     menu_items = Menu().get_items()
#     order = input(f"What would you like? {menu_items}: ")
#     if order == "off":
#         is_on = False
#     elif order == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink_order = Menu().find_drink(order)
#         if coffee_maker.is_resource_sufficient(drink_order):
#             if money_machine.make_payment(drink_order.cost):
#                 coffee_maker.make_coffee(drink_order)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
