"""Calculator state and operations used by the Tkinter app."""


class CalculatorState:
    """Manage display text, pending operators, and calculation behavior."""

    def __init__(self):
        self.display = "0"
        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_number = False

    def clear(self):
        self.display = "0"
        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_number = False
        return self.display

    def input_digit(self, digit):
        if self.display == "Error" or self.waiting_for_number:
            self.display = digit
            self.waiting_for_number = False
        elif self.display == "0":
            self.display = digit
        else:
            self.display += digit

        return self.display

    def input_decimal(self):
        if self.display == "Error" or self.waiting_for_number:
            self.display = "0."
            self.waiting_for_number = False
        elif "." not in self.display:
            self.display += "."

        return self.display

    def toggle_sign(self):
        if self.display == "Error":
            return self.clear()

        if self.display == "0":
            return self.display

        if self.display.startswith("-"):
            self.display = self.display[1:]
        else:
            self.display = "-" + self.display

        return self.display

    def backspace(self):
        if self.display == "Error" or self.waiting_for_number:
            return self.clear()

        if len(self.display) <= 1 or (self.display.startswith("-") and len(self.display) == 2):
            self.display = "0"
        else:
            self.display = self.display[:-1]

        return self.display

    def set_operator(self, operator):
        if self.display == "Error":
            self.clear()

        current_value = float(self.display)

        if self.pending_operator and not self.waiting_for_number:
            result = self._calculate(self.stored_value, current_value, self.pending_operator)

            if result is None:
                self.display = "Error"
                self.stored_value = None
                self.pending_operator = None
                self.waiting_for_number = True
                return self.display

            self.stored_value = result
            self.display = self._format_number(result)
        else:
            self.stored_value = current_value

        self.pending_operator = operator
        self.waiting_for_number = True
        return self.display

    def calculate(self):
        if self.pending_operator is None or self.stored_value is None:
            return self.display

        current_value = float(self.display)
        result = self._calculate(self.stored_value, current_value, self.pending_operator)

        if result is None:
            self.display = "Error"
        else:
            self.display = self._format_number(result)

        self.stored_value = None
        self.pending_operator = None
        self.waiting_for_number = True
        return self.display

    def _calculate(self, left, right, operator):
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        if operator == "/":
            if right == 0:
                return None
            return left / right

        raise ValueError(f"Unsupported operator: {operator}")

    def _format_number(self, value):
        if value.is_integer():
            return str(int(value))
        return str(round(value, 10)).rstrip("0").rstrip(".")
