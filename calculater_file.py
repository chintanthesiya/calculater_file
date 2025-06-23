history_file = "history.txt"

def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found.")
            else:
                print("Calculation History:")
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found yet.")

def clear_history():
    with open(history_file, 'w') as file:
        pass  # Just open and close to clear content
    print("History cleared.")

def save_to_history(equation, result):
    with open(history_file, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid number format.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    # Convert to int if no decimal part
    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("Simple Calculator (type 'history', 'clear', or 'exit')")
    while True:
        user_input = input("\nEnter calculation (+, -, *, /) or command: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()
