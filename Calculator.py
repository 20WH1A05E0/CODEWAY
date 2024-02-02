def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user operation choice
choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice in ['1', '2', '3', '4']:
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    # Display the result
    print(f"Result: {result}")

else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")
import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}")

    except ValueError:
        label_result.config(text="Error: Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input widgets
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

operation_var = tk.StringVar(value="Addition")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
dropdown_operation = tk.OptionMenu(root, operation_var, *operations)
dropdown_operation.grid(row=0, column=2, padx=5, pady=5)

# Create button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

# Create label to display result
label_result = tk.Label(root, text="Result:")
label_result.grid(row=2, column=0, columnspan=3)

# Start the main loop
root.mainloop()

