import dictionary

coffee_machine_is_working = True
total_money = 0
total_milk = 200
total_coffee = 100
total_water = 300

def processing_money():
    global  total_money
    print('Please insert coins:')
    total_money = float(input("how many quarters?: ")) * 0.25
    total_money += float(input("how many dimes?: ")) * 0.1
    total_money += float(input("how many nickles?: ")) * 0.05
    total_money += float(input("how many pennies?: ")) * 0.01
    return  total_money

while coffee_machine_is_working:
    next_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if next_order == 'latte' or next_order == 'cappuccino':
        if total_coffee < dictionary.MENU[next_order]["ingredients"]["coffee"]:
            print("Sorry that's not enough coffee in machine. Money will be refunded.")
        elif total_milk < dictionary.MENU[next_order]["ingredients"]["milk"]:
            print("Sorry that's not enough milk in machine. Money will be refunded.")
        elif total_water < dictionary.MENU[next_order]["ingredients"]["water"]:
            print("Sorry that's not enough water in machine. Money will be refunded.")
        else:
            processing_money()
            if dictionary.MENU[next_order]["cost"] <= total_money:
                if (total_water >= dictionary.MENU[next_order]["ingredients"]["water"]
                        and total_milk >= dictionary.MENU[next_order]["ingredients"]["milk"]
                        and total_coffee >= dictionary.MENU[next_order]["ingredients"]["coffee"]):
                    change = round(total_money - dictionary.MENU[next_order]["cost"], 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {next_order} ☕️.Enjoy!")
                    total_water = total_water - (dictionary.MENU[next_order]["ingredients"]["water"])
                    total_coffee = total_coffee - (dictionary.MENU[next_order]["ingredients"]["coffee"])
                    total_milk = total_milk - (dictionary.MENU[next_order]["ingredients"]["milk"])
                    total_money = 0
            else:
                print("Sorry that's not enough money. Money will be refunded.")
    elif next_order == 'espresso':
        if total_coffee < dictionary.MENU[next_order]["ingredients"]["coffee"]:
            print("Sorry that's not enough coffee in machine. Money will be refunded.")
        elif total_water < dictionary.MENU[next_order]["ingredients"]["water"]:
            print("Sorry that's not enough water in machine. Money will be refunded.")
        else:
            processing_money()

            if dictionary.MENU[next_order]["cost"] <= total_money:
                if total_water >= dictionary.MENU[next_order]["ingredients"]["water"] and total_coffee >= dictionary.MENU[next_order]["ingredients"]["coffee"]:
                    change = round(total_money - dictionary.MENU[next_order]["cost"], 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {next_order} ☕️.Enjoy!")
                    total_water = total_water - (dictionary.MENU[next_order]["ingredients"]["water"])
                    total_coffee = total_coffee - (dictionary.MENU[next_order]["ingredients"]["coffee"])
                    total_money = 0
            else:
                print("Sorry that's not enough money. Money will be refunded.")
    elif next_order == 'report':
        print(f"Water: {total_water}ml\n"
              f"Milk: {total_milk}ml\n"
              f"Coffee: {total_coffee}g\n"
              f"Money: ${total_money}")
    elif next_order == "off":
        coffee_machine_is_working = False
