from tkinter import *

def calculate():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    operator = operator_var.get()

    if operator == "Add":
        result = num1 + num2
    elif operator == "Subtract":
        result = num1 - num2
    elif operator == "Multiply":
        result = num1 * num2
    elif operator == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero!"
    else:
        result = "Invalid operator. Please choose a valid option."

    label_result.config(text="Result: " + str(result))

def quit_program():
    root.destroy()

root = Tk()
root.title("Simple Calculator")

label_title = Label(root, text="SIMPLE CALCULATOR", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

entry_num1 = Entry(root, width=15)
entry_num1.pack()

entry_num2 = Entry(root, width=15)
entry_num2.pack()

operator_var = StringVar(root)
operator_var.set("Operator")

operator_label = Label(root, text="Choose an operator:", font=("Arial", 10, "bold"))
operator_label.pack()

operator_menu = OptionMenu(root, operator_var, "Add", "Subtract", "Multiply", "Divide")
operator_menu.pack()

button_calculate = Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

label_result = Label(root, text="Result: ", font=("Arial", 10, "bold"))
label_result.pack()

button_quit = Button(root, text="Quit", command=quit_program)
button_quit.pack(pady=10)

root.mainloop()
