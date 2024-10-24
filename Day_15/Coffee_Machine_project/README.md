# Coffee Machine Program

## Program Overview
This program simulates a coffee machine that allows users to purchase drinks like espresso, latte, and cappuccino. The machine checks if it has enough resources (water, milk, coffee) and processes user payments using coin input.

### Main Flow of the Program
1. **User Interaction Loop**: 
   - The program continuously prompts the user to select a drink or request a report of the current resources.
   - The loop ends when the user inputs `"off"` to turn off the machine.

2. **Check Resources**: 
   - The program checks if there are enough resources to make the selected drink before proceeding.
   - If there are not enough resources (e.g., insufficient water), the program prints a specific message and does not proceed.

3. **Process Coins**:
   - After confirming enough resources, the machine asks the user to insert coins.
   - The total amount of money inserted is calculated and checked against the cost of the drink.

4. **Deduct Resources and Serve the Drink**:
   - If the user inserts enough money, the machine deducts the required resources, updates the machine’s total money, and serves the drink.
   - If insufficient money is inserted, the machine refunds the user.

---

## Functions and How They Work

### 1. `check_resources()`
**Purpose**: Verifies if the machine has enough resources to make the selected drink.

**How it works**:
- Compares the required ingredients for the drink (from the `MENU`) with the available resources.
- If any resource is insufficient, it prints a message like `"Sorry, there is not enough water"`, and returns `False`.
- If all resources are sufficient, it returns `True`.

### 2. `process_coins()`
**Purpose**: Handles the collection of coins and checks if enough money is inserted.

**How it works**:
- Prompts the user to insert quarters, dimes, nickels, and pennies.
- Calculates the total value of the inserted coins.
- If the total is less than the drink's cost, it refunds the money.
- If the total is more than the drink's cost, it returns the change and allows the transaction to proceed.

### 3. `print_report()`
**Purpose**: Displays the current status of resources and total money collected.

**How it works**:
- Prints the values of water, milk, coffee, and total money from the machine's resources.

---

## Detailed Program Flow

1. **User Input**:
   - The machine prompts the user to select a drink, check the report, or turn off the machine.

2. **Handle `off` and `report` Commands**:
   - If the user inputs `"off"`, the program exits.
   - If the user inputs `"report"`, the current resources and money are displayed using the `print_report()` function.

3. **Check Resources**:
   - When a drink is selected, the machine calls `check_resources()` to ensure enough resources are available.
   - If not, it prints an error and stops the transaction.

4. **Process Coins**:
   - If resources are sufficient, the machine calls `process_coins()` to collect money.
   - If the payment is successful, it deducts the resources and serves the drink.
   - If the payment fails, the machine refunds the money and stops.

5. **Update Resources and Serve**:
   - After successful payment, the machine updates the resources and prints a message saying the drink is served.

---

## Summary
This coffee machine program allows users to:
- Select a drink.
- The program verifies if enough resources are available.
- The program processes coin input, checks if sufficient money is inserted, and then serves the drink if all conditions are met.
