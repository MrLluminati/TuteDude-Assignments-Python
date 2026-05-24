# Simple Calculator using Tkinter

import tkinter as tk

# Create the main window

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

# Create the display for the calculator

display = tk.Entry(window, width=25, font=("Arial", 18), justify="right")
display.pack(pady=20)

# Variables to store the first number, operator, and second number

first_number = ""
operator = ""
second_number = ""

# Create a frame for the buttons

button_frame = tk.Frame(window)
button_frame.pack()

# Functions for button clicks

## Function to handle number button clicks
 
def click_number(number):
    global first_number
    global second_number
    global operator

    if operator == "":
        first_number = first_number + number
    else:
        second_number = second_number + number
    
    display.insert(tk.END, number)

## Function to clear the display

def clear_display():
    global first_number
    global second_number
    global operator

    first_number = ""
    second_number = ""
    operator = ""

    display.delete(0, tk.END)

## Function to handle operator button clicks

def click_operator(selected_operator):
    global operator

    if first_number != "" and operator == "":
        operator = selected_operator
        display.insert(tk.END, selected_operator)

## Function to calculate the result when the equals button is clicked

def calculate_result():
    global first_number
    global second_number
    global operator

    if first_number == "" or operator == "" or second_number == "":
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        return
    num1 = float(first_number)
    num2 = float(second_number)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            return
        result = num1 / num2
    else:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        return
    
    display.delete(0, tk.END)
    display.insert(tk.END, result)

    first_number = str(result)
    operator = ""
    second_number = ""

# Buttons for numbers and operators

button_1 = tk.Button(button_frame, text="1", width=5, height=2, command=lambda: click_number("1"))
button_1.grid(row=0, column=0)

button_2 = tk.Button(button_frame, text="2", width=5, height=2, command=lambda: click_number("2"))
button_2.grid(row=0, column=1)

button_3 = tk.Button(button_frame, text="3", width=5, height=2, command=lambda: click_number("3"))
button_3.grid(row=0, column=2)

button_4 = tk.Button(button_frame, text="4", width=5, height=2, command=lambda: click_number("4"))
button_4.grid(row=1, column=0)

button_5 = tk.Button(button_frame, text="5", width=5, height=2, command=lambda: click_number("5"))
button_5.grid(row=1, column=1)

button_6 = tk.Button(button_frame, text="6", width=5, height=2, command=lambda: click_number("6"))
button_6.grid(row=1, column=2)

button_7 = tk.Button(button_frame, text="7", width=5, height=2, command=lambda: click_number("7"))
button_7.grid(row=2, column=0)

button_8 = tk.Button(button_frame, text="8", width=5, height=2, command=lambda: click_number("8"))
button_8.grid(row=2, column=1)

button_9 = tk.Button(button_frame, text="9", width=5, height=2, command=lambda: click_number("9"))
button_9.grid(row=2, column=2)

button_0 = tk.Button(button_frame, text="0", width=5, height=2, command=lambda: click_number("0"))
button_0.grid(row=3, column=1)

clear_button = tk.Button(button_frame, text="C", width=5, height=2, command=clear_display)
clear_button.grid(row=3, column=0)

plus_button = tk.Button(button_frame, text="+", width=5, height=2, command=lambda: click_operator("+"))
plus_button.grid(row=0, column=3)

minus_button = tk.Button(button_frame, text="-", width=5, height=2, command=lambda: click_operator("-"))
minus_button.grid(row=1, column=3)

multiply_button = tk.Button(button_frame, text="*", width=5, height=2, command=lambda: click_operator("*"))
multiply_button.grid(row=2, column=3)

divide_button = tk.Button(button_frame, text="/", width=5, height=2, command=lambda: click_operator("/"))
divide_button.grid(row=3, column=3)

equals_button = tk.Button(button_frame, text="=", width=5, height=2, command=calculate_result)
equals_button.grid(row=3, column=2)

# Start the main event loop

window.mainloop()
