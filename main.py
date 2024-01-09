import tkinter as tk

# it will create the main window for the calculator
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the input and it will also shows the result in same widget
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Placeholder
button_layout = []

root.mainloop()
