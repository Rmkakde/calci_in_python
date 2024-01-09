import tkinter as tk

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)


# Function to evaluate and display the result
def evaluate_expression():
    try:
        result = eval(entry.get()) # it will evaluate the expression entered in the entry widget
        entry.delete(0, tk.END)  # Clear the entry widget and insert the result in the widget
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END) # If an error occurs during evaluation,It will clear the entry widget and display "Error"
        entry.insert(tk.END, "Error")


# Function to handle button clicks
def button_click(value):
    current = entry.get()
    
    if value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + str(value))
        
# it will create the main window for the calculator
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the input and it will also shows the result in same widget
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Placeholder
button_layout = []

root.mainloop()
