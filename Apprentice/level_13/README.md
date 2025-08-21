## Level 13: Coffee Machine (OOP)

In this level you will wire up a simple coffee machine using object‑oriented building blocks. You will interact with three modules—`Menu`, `CoffeeMaker`, and `MoneyMachine`—to: query available drinks, check resources, process payments, and brew coffee.

**How to run:**

1. Create the following files in the same folder:

   -`menu.py` (defines `Menu` and `MenuItem`).

   -`coffee_maker.py`(defines `CoffeeMaker`).

   -`money_machine.py` (defines `MoneyMachine`).

2. Save the main code as `main.py`.

3. Run the command:

   ```bash
   python main.py
   ```

4. Type a drink name from the menu options (e.g., `latte`, `espresso`, `capuccino`), or `report/off`.

**Learning objectives:**

- Use multiple classes to model a system (menu, machine, payment).
- Practice method design (`report`, `find_drink`, `is_resource_sufficient`, `make_payment`, `make_coffee`)
- Manage program flow with a REPL‑style loop and user input.
- Keep logic decoupled and testable by separating concerns into modules.
