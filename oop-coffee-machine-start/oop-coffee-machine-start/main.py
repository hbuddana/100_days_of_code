from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Importing the necessary classes for handling the menu, coffee maker resources, and money machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize instances of Menu, CoffeeMaker, and MoneyMachine classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Main program loop to keep the coffee machine running until turned off
while True:
    # Get the list of available drink options and display them in the user prompt
    options = menu.get_items()
    user_ip = input(f"What would you like? ({options}): ")

    # Handle the case where the user wants to turn off the machine
    if user_ip == "off":
        break  # Exit the loop, ending the program

    # Handle the case where the user wants a status report on resources and money
    elif user_ip == "report":
        coffee_maker.report()  # Prints current resources (water, milk, coffee)
        money_machine.report()  # Prints the total profit collected so far

    # Handle drink selection
    else:
        # Find the selected drink in the menu
        drink = menu.find_drink(user_ip)

        # Check if resources are sufficient for the selected drink
        # Then check if payment is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # If both resource check and payment are successful, make the coffee
            coffee_maker.make_coffee(drink)

