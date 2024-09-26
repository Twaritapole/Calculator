import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation."
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main application window
root = tk.Tk()
root.title("Funny Calculator")
root.geometry("400x400")
root.config(bg="#FFCC00")  # Bright yellow background

# Create a fun title label
title_label = tk.Label(root, text="🎉 Fun Calculator 🎉", font=("Comic Sans MS", 20), bg="#FFCC00", fg="#FF5733")
title_label.pack(pady=20)

# Create input fields with quirky labels
entry_num1_label = tk.Label(root, text="Enter First Number 🍭", font=("Comic Sans MS", 14), bg="#FFCC00")
entry_num1_label.pack()
entry_num1 = tk.Entry(root, font=("Arial", 14), width=10)
entry_num1.pack(pady=5)

entry_num2_label = tk.Label(root, text="Enter Second Number 🍬", font=("Comic Sans MS", 14), bg="#FFCC00")
entry_num2_label.pack()
entry_num2 = tk.Entry(root, font=("Arial", 14), width=10)
entry_num2.pack(pady=5)

# Create operation selection
operation_var = tk.StringVar(value='Add')  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, 'Add', 'Subtract', 'Multiply', 'Divide')
operation_menu.config(font=("Arial", 14), bg="#FF5733", fg="#FFFFFF")
operation_menu.pack(pady=10)

# Create a funny calculate button
calculate_button = tk.Button(root, text="🧮 Calculate! 🧮", command=calculate, font=("Arial", 16), bg="#28B463", fg="white")
calculate_button.pack(pady=20)

# Create result label with a fun style
result_label = tk.Label(root, text="Result: ", font=("Comic Sans MS", 16), bg="#FFCC00", fg="#FF5733")
result_label.pack(pady=10)

# Run the application
root.mainloop()
