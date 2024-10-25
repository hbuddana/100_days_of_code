# Coffee Machine Program (OOP Implementation)

This program simulates a coffee machine using Object-Oriented Programming (OOP) principles with classes for managing the menu, coffee maker resources, and payment processing.

## Code Structure and Explanation

1. **Initialize Classes**:
   - Create instances of `Menu`, `CoffeeMaker`, and `MoneyMachine` to manage drinks, resources, and payment.

2. **Main Program Loop**:
   - Keeps the coffee machine running until the user inputs `"off"`.

3. **User Actions**:
   - **Get Available Options**: Use `menu.get_items()` to display drink options in the prompt.
   - **Turn Off (`"off"`)**: Exit the loop, shutting down the coffee machine.
   - **Report (`"report"`)**: Print the current resources and total money collected by calling `coffee_maker.report()` and `money_machine.report()`.

4. **Drink Selection**:
   - **Find Drink**: Use `menu.find_drink(user_ip)` to retrieve the selected drink.
   - **Check Resources**: Call `coffee_maker.is_resource_sufficient(drink)` to ensure enough ingredients.
   - **Process Payment**: Call `money_machine.make_payment(drink.cost)` to verify sufficient payment.

5. **Make Coffee**:
   - If resources and payment are sufficient, `coffee_maker.make_coffee(drink)` is called to serve the drink and deduct the ingredients.

---

