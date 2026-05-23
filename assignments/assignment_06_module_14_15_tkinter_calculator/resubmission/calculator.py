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

button_1 = tk.Button(button_frame, text="1", width=5, height=2, command=lambda: click_number("1"))
button_1.grid(row=0, column=0)

button_2 = tk.Button(button_frame, text="2", width=5, height=2, command=lambda: click_number("2"))
button_2.grid(row=0, column=1)

button_3 = tk.Button(button_frame, text="3", width=5, height=2, command=lambda: click_number("3"))
button_3.grid(row=0, column=2)

window.mainloop()