from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
menu_items = coffee_menu.get_items()
cash_calc = MoneyMachine()


def keurig():
    machine_on = True
    while machine_on:
        customer_order = input(f"What would you like? ({menu_items}): ").lower()
        if customer_order == "report":
            coffee_machine.report()
            cash_calc.report()
        elif customer_order == "off":
            machine_on = False
        else:
            item = coffee_menu.find_drink(customer_order)
            if item != "none":
                can_make = coffee_machine.is_resource_sufficient(item)
                if can_make is True:
                    for x in coffee_menu.menu:
                        if x == item:
                            price = item.cost
                    accept_payment = cash_calc.make_payment(price)
                    if accept_payment is True:
                        coffee_machine.make_coffee(item)


keurig()

