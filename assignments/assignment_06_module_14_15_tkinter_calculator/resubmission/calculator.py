import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

display = tk.Entry(window, width=25, font=("Arial", 18), justify="right")
display.pack(pady=20)

window.mainloop()