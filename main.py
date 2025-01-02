from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def coffee_machine_maker():
    obj_coffeemaker = CoffeeMaker()
    obj_menu = Menu()
    obj_menuItem = MenuItem("name", 'water','milk','coffee', 'cost')
    obj_moneyMachine = MoneyMachine()
    is_on = True

    while is_on:
        options = obj_menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            print("Machine turned off")
            is_on = False
        elif choice == 'report':
            obj_coffeemaker.report()
            obj_moneyMachine.report()
        else:
            drink = obj_menu.find_drink(choice)
            if obj_coffeemaker.is_resource_sufficient(drink) and obj_moneyMachine.make_payment(drink.cost):
                    obj_coffeemaker.make_coffee(drink)


coffee_machine_maker()