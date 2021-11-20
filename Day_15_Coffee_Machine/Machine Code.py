from main import machine_resources
from main import MENU
from art import logo

# Prints Coffee Shop Logo
print(logo)


# Takes inserted money.
def insert_change(user_order):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    # Calculates amount of coins inserted.
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    # If inserted amount is less than the menu item the customer ordered,  refund the coins.
    if total < MENU[user_order]["cost"]:
        print("\nYou inserted ", "$", round(total, 2), sep='')
        print("The ", user_order, " costs $", MENU["latte"]["cost"], sep='')
        print("Sorry that's not enough money. Wait while we return your coins...")
    # If the inserted amount is
    else:
        menu_item_cost = MENU[user_order]["cost"]
        user_change = total - menu_item_cost
        print("\nHere is $", round(user_change, 2), " in change.",  sep='')
        print("Here is your", user_order, "☕" ". Enjoy!")
        get_user_order()


def check_resources(menu_item):
    # Loops through ingredients in the menu item using the customers order (menu_item)
    for x in MENU[menu_item]["ingredients"]:
        # If there aren't enough resources to make the order, prints error message.
        if machine_resources[x] < MENU[menu_item]["ingredients"][x]:
            print("Sorry, not enough", x, "to make", menu_item)
            return get_user_order()
    # If there are sufficient resources, makes order and subtracts resources.
    for x in MENU[menu_item]["ingredients"]:
        if machine_resources[x] > MENU[menu_item]["ingredients"][x]:
            new_value = machine_resources[x] - MENU[menu_item]["ingredients"][x]
            machine_resources[x] = new_value
    machine_resources["money"] += MENU[menu_item]["cost"]


def resource_formatter(resource_key):
    # Formats report with the correct unit type (ml).
    if resource_key == "water" or resource_key == "milk":
        print(resource_key.capitalize(), ": ", machine_resources[resource_key], "ml", sep='')
    # Formats report with the correct unit type (g).
    elif resource_key == "coffee":
        print(resource_key.capitalize(), ": ", machine_resources[resource_key], "g", sep='')
    # Formats report with the correct unit type ($).
    elif resource_key == "money":
        print(resource_key.capitalize(), ": ", "$", machine_resources[resource_key], sep='')


def get_user_order():
    # Get order from customer.
    user_order = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    # User Input Validation.
    if user_order == "espresso":
        check_resources(user_order)
        insert_change(user_order)
    elif user_order == "latte":
        check_resources(user_order)
        insert_change(user_order)
    elif user_order == "cappuccino":
        check_resources(user_order)
        insert_change(user_order)
    # Print out list of current machine resources.
    elif user_order == "report":
        for key in machine_resources:
            resource_formatter(key)
        get_user_order()
    # Turns off the machine.
    elif user_order == "off":
        return
    # Prompts customer to enter valid item, if order is not one of the menu items.
    else:
        print("Enter a valid menu item...")
        get_user_order()


get_user_order()



