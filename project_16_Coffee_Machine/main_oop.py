from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drink = MenuItem
machine_is_on = True
while machine_is_on:
    available_options = menu.get_items()
    user_next_order = input(f"What would you like? {available_options}: ").lower()
    if user_next_order == "off":
        machine_is_on = False
    elif user_next_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=user_next_order) #Searches the menu for a particular drink by name.
        # Returns a MenuItem object if it exists, otherwise returns None.
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





