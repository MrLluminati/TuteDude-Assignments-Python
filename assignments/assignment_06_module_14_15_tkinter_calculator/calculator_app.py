"""Tkinter calculator application for Assignment 6."""

import tkinter as tk
from tkinter import ttk

from calculator_logic import CalculatorState


class CalculatorApp:
    """Build and run the calculator GUI."""

    def __init__(self, root):
        self.root = root
        self.state = CalculatorState()
        self.display_var = tk.StringVar(value=self.state.display)

        self._configure_window()
        self._build_display()
        self._build_buttons()

    def _configure_window(self):
        self.root.title("Tkinter Calculator")
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)

    def _build_display(self):
        display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            justify="right",
            font=("Segoe UI", 20),
            state="readonly",
            width=18,
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 8), sticky="ew")

    def _build_buttons(self):
        buttons = [
            ("C", self.clear), ("<-", self.backspace), ("+/-", self.toggle_sign), ("/", lambda: self.operator("/")),
            ("7", lambda: self.digit("7")), ("8", lambda: self.digit("8")), ("9", lambda: self.digit("9")), ("*", lambda: self.operator("*")),
            ("4", lambda: self.digit("4")), ("5", lambda: self.digit("5")), ("6", lambda: self.digit("6")), ("-", lambda: self.operator("-")),
            ("1", lambda: self.digit("1")), ("2", lambda: self.digit("2")), ("3", lambda: self.digit("3")), ("+", lambda: self.operator("+")),
            ("0", lambda: self.digit("0")), (".", self.decimal), ("=", self.calculate),
        ]

        row = 1
        column = 0

        for label, command in buttons:
            column_span = 2 if label == "=" else 1
            button = ttk.Button(self.root, text=label, command=command, width=8)
            button.grid(row=row, column=column, columnspan=column_span, padx=4, pady=4, sticky="nsew")

            column += column_span

            if column >= 4:
                column = 0
                row += 1

        for index in range(4):
            self.root.columnconfigure(index, weight=1)

    def _sync_display(self, value):
        self.display_var.set(value)

    def digit(self, digit):
        self._sync_display(self.state.input_digit(digit))

    def decimal(self):
        self._sync_display(self.state.input_decimal())

    def operator(self, operator):
        self._sync_display(self.state.set_operator(operator))

    def calculate(self):
        self._sync_display(self.state.calculate())

    def clear(self):
        self._sync_display(self.state.clear())

    def backspace(self):
        self._sync_display(self.state.backspace())

    def toggle_sign(self):
        self._sync_display(self.state.toggle_sign())


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
