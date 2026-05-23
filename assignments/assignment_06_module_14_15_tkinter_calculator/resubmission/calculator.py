import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

display = tk.Entry(window, width=25, font=("Arial", 18), justify="right")
display.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack()

def click_number(number):
    display.insert(tk.END, number)

def clear_display():
    display.delete(0, tk.END)

def click_operator(operator):
    display.insert(tk.END, operator)

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

window.mainloop()