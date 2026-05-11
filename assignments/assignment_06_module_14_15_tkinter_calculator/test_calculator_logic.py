"""Basic validation tests for the calculator logic."""

import unittest

from calculator_logic import CalculatorState


class CalculatorStateTests(unittest.TestCase):
    def test_addition(self):
        state = CalculatorState()
        state.input_digit("1")
        state.input_digit("2")
        state.set_operator("+")
        state.input_digit("8")

        self.assertEqual(state.calculate(), "20")

    def test_decimal_multiplication(self):
        state = CalculatorState()
        state.input_digit("2")
        state.input_decimal()
        state.input_digit("5")
        state.set_operator("*")
        state.input_digit("4")

        self.assertEqual(state.calculate(), "10")

    def test_division_by_zero(self):
        state = CalculatorState()
        state.input_digit("9")
        state.set_operator("/")
        state.input_digit("0")

        self.assertEqual(state.calculate(), "Error")

    def test_clear_after_error(self):
        state = CalculatorState()
        state.input_digit("9")
        state.set_operator("/")
        state.input_digit("0")
        state.calculate()

        self.assertEqual(state.clear(), "0")

    def test_backspace(self):
        state = CalculatorState()
        state.input_digit("4")
        state.input_digit("2")

        self.assertEqual(state.backspace(), "4")


if __name__ == "__main__":
    unittest.main()
