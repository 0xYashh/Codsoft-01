import tkinter as tk
from tkinter import messagebox

# Function to perform calculations
def calculate():
    num1 = entry1.get()
    num2 = entry2.get()
    operation = operation_var.get()

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")
        clear()
        return

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Math error", "Cannot divide by zero.")
            clear()
            return
    else:
        messagebox.showerror("Operation error", "Invalid operation.")
        return

    result_entry.config(state=tk.NORMAL)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(result))
    result_entry.config(state="readonly")

# Function to clear all inputs and result
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_entry.config(state=tk.NORMAL)
    result_entry.delete(0, tk.END)
    result_entry.config(state="readonly")

# Create main window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# Input fields for numbers
entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root, width=15)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Operation dropdown menu
operation_var = tk.StringVar(value='+')
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Calculate and Clear buttons
calc_button = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", width=10)
calc_button.grid(row=3, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear, bg="#f44336", fg="white", width=10)
clear_button.grid(row=3, column=1, padx=10, pady=10)

# Label and entry to display the result
result_label = tk.Label(root, text="Result:", bg="#f0f0f0")
result_label.grid(row=4, column=0, padx=10, pady=10)

result_entry = tk.Entry(root, width=20, state="readonly")
result_entry.grid(row=4, column=1, padx=10, pady=10)

# Labels for input fields
label1 = tk.Label(root, text="First number:", bg="#f0f0f0")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Second number:", bg="#f0f0f0")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Operation:", bg="#f0f0f0")
label3.grid(row=2, column=0)

# Start the main loop
root.mainloop()
