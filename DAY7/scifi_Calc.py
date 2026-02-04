def adv_calculator():
    actions = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else 'Error: Division by zero',
        'power': lambda x, y: x ** y
    }
    print("Welcome to the Advanced Calculator!")
    print("Available operations: add, subtract, multiply, divide, power")
    while True:
        action = input("Enter operation (or 'exit' to quit): ").strip().lower()
        if action == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if action not in actions:
            print("Invalid operation. Please try again.")
            continue
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = actions[action](x, y)
            print(f"The result of {action}ing {x} and {y} is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")


adv_calculator()
