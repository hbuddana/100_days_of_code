# Coffee machine menu and initial resources
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

resources = {"water": 300, "milk": 200, "coffee": 100}  # Initial resources available
money = 0  # Starting with no money collected

# Function to print the report of the machine's current resources and total money
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# Function to check if there are sufficient resources for the selected drink
def check_resources(ingredients):
    # Loop through each ingredient (water, milk, coffee) and check if it's available
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False  # Return False if any resource is insufficient
    return True  # Return True if all resources are sufficient

# Function to process coins and calculate total money inserted
def process_coins():
    print("Please insert coins.")
    # Asking the user to input the number of quarters, dimes, nickels, and pennies
    quarters = int(input("How many quarters?: "))  # 0.25
    dimes = int(input("How many dimes?: "))        # 0.10
    nickels = int(input("How many nickels?: "))    # 0.05
    pennies = int(input("How many pennies?: "))    # 0.01
    
    # Calculate the total amount of money inserted by the user
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

# Function to make the coffee and deduct the resources used
def make_coffee(drink, ingredients):
    # Deduct each ingredient from the available resources
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")  # Serve the coffee to the user

# Main program loop
while True:
    # Prompting the user for an action (choose a drink, report, or turn off the machine)
    user_ip = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

    # Check if the user wants to turn off the machine
    if user_ip == "off":
        break  # Exit the loop, turning off the machine
    
    # Check if the user requested a report of resources
    elif user_ip == "report":
        print_report()  # Print the current resource report
    
    # Check if the user selected a valid drink option
    elif user_ip in MENU:
        drink = MENU[user_ip]  # Get the selected drink's information (ingredients and cost)
        
        # Step 1: Check if there are enough resources to make the selected drink
        if check_resources(drink["ingredients"]):
            # Step 2: Process the coins and calculate the total amount inserted by the user
            payment = process_coins()
            
            # Step 3: Check if the inserted money is enough to buy the drink
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)  # Calculate the change to return
                if change > 0:
                    print(f"Here is ${change} in change.")  # Return change if overpayment
                
                # Add the drink's cost to the total money collected by the machine
                #global money
                money += drink["cost"]
                
                # Step 4: Deduct the resources and serve the drink
                make_coffee(user_ip, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")  # Refund if not enough money
    else:
        print("Invalid selection. Please choose a valid option.")  # Handle invalid user input


"""How This Code is More Efficient and Clear:

Loops for Resource Handling: Both checking and deducting resources are handled dynamically through loops, making the code more flexible.

Separation of Concerns: Each function has a single responsibility (e.g., check_resources only checks, make_coffee only handles resource deduction), 
which makes the code easier to understand, debug, and extend.

Commenting: The comments provide clarity on each major step, making the flow of the program easier to follow for others (or your future self)."""