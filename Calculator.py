import tkinter as tk


def evaluate():
    try:
        user_input = entry.get()
        output = eval(user_input)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(output))


    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def clear_entry():
    entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create button widgets
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: entry.insert(tk.END,
                                                                                            b) if b != "=" and b != "C" else evaluate() if b == "=" else clear_entry()).grid(
        row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the event loop
window.mainloop()
