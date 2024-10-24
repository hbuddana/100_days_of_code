MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources in the machine 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# Get_report - Reports all the available resources in the machine 
def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources ['milk']}ml")
    print(f"Coffee: {resources ['coffee']}ml")
    print(f"Money:${money}")

# Checks if the resources are sufficient or not, if True then checks for the coins and then gives the drink
def check_resources():
    water_avail = (resources['water'] >= MENU[user_ip]["ingredients"]["water"])
    milk_avail = (resources['milk'] >= MENU[user_ip]["ingredients"]["milk"])
    coffee_avail = (resources['coffee'] >= MENU[user_ip]["ingredients"]["coffee"])
    
    if not water_avail:
        print("Sorry, there is not enough water")
        return False  # Early return if water is insufficient
    elif not milk_avail:
        print("Sorry, there is not enough milk")
        return False  # Early return if milk is insufficient
    elif not coffee_avail:
        print("Sorry, there is not enough coffee")
        return False  # Early return if coffee is insufficient
    
    return True 

    

# # Function to process coins and return the total amount
def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    
    # Calculate total money inserted
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    drink_cost = MENU[user_ip]["cost"]
    
    if total < drink_cost:
        print("Sorry that's not enough money. Money Refunded")
        return False
    elif total > drink_cost:
        change = round(total - drink_cost, 2)
        print(f"Here is ${change}💲in change")
        print(f"Here is your {user_ip} 🍵☕. Enjoy")
        return change
    
    elif total == drink_cost:
        print(f"Here is your {user_ip}. Enjoy")
        
        
    

# Prompt and Entry point of the program 
while True:
    user_ip = input("What would you like? (espresso/latte/cappuccino):")
    

    if user_ip == "off":
        break # Shut down the coffee machine
    elif user_ip == "report":
        get_report()
        
    elif user_ip in MENU:  # If the user selected a valid drink
        if check_resources():  # Step 1: Check if there are enough resources
            if process_coins():  # Step 2: Check if the user inserted enough money
                # Step 3: Deduct resources and serve the drink
                resources['water'] -= MENU[user_ip]["ingredients"]["water"]
                resources['milk'] -= MENU[user_ip]["ingredients"]["milk"]
                resources['coffee'] -= MENU[user_ip]["ingredients"]["coffee"]
                money += MENU[user_ip]["cost"]  # Add the cost of the drink to the total money
                #print(f"Here is your {user_ip}. Enjoy!")
    else:
        print("Invalid selection. Please choose a valid option.")
    
