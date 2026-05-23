# Assignment 6 Resubmission: Tkinter Calculator

## Resubmission Reason

The earlier Tkinter calculator submission was rejected because it appeared too polished and did not clearly show my own learning process. The feedback specifically asked me to rework the calculator in a simpler beginner-level style and show my actual thought process, mistakes, debugging, and gradual improvement.

This resubmission is being rebuilt step by step in a simpler way so that I can understand Tkinter, event handling, and basic state management properly.

## AI Usage Note

In earlier tasks, AI assistance was used for general understanding, code cleanup, and making submissions more presentable. After receiving mentor feedback, I understood that the main purpose of this assignment is to learn by building the project myself.

For this resubmission, AI is being used only for conceptual guidance, debugging support, and learning direction where needed. The code is being rebuilt incrementally by me in a beginner-friendly style.

## Current File

| File | Purpose |
| --- | --- |
| [`calculator.py`](calculator.py) | Beginner-level Tkinter calculator rebuilt step by step. |
| [`screenshot_proofs/`](screenshot_proofs/) | Screenshots showing progress, mistakes, fixes, and outputs. |

---

## Step 1: Basic Tkinter Window and Display Box

### What I did

In this step, I started rebuilding the calculator from the beginning.

I created:

- a Tkinter window,
- a window title,
- a fixed window size,
- one `Entry` widget to work as the calculator display,
- the `mainloop()` required to keep the window open.

### Mistakes and debugging

During this step, I made some basic mistakes:

- I typed `notpad` instead of `notepad`.
- I typed `import tkinter as tk` directly into PowerShell instead of inside the Python file.
- I ran `python .` instead of running the actual file using `python .\calculator.py`.
- I wrote `windo.geometry(...)` instead of `window.geometry(...)`, which caused a `NameError`.

### How I fixed it

I corrected the command mistakes, moved the Python code into `calculator.py`, ran the correct file, and fixed `windo` to `window`.

### Code completed in Step 1

```python
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

display = tk.Entry(window, width=25, font=("Arial", 18), justify="right")
display.pack(pady=20)

window.mainloop()
```

### What I learned

- `tk.Tk()` creates the main application window.
- `window.title()` sets the title of the window.
- `window.geometry()` controls the size of the window.
- `tk.Entry()` creates a text/display box.
- `pack()` places the widget inside the window.
- `mainloop()` keeps the Tkinter window running.

### Screenshot proof

- [Terminal mistakes and `NameError`](screenshot_proofs/step_01_basic_window/step_01_a_terminal_mistakes_and_nameerror.png)
- [Corrected basic window code](screenshot_proofs/step_01_basic_window/step_01_b_corrected_basic_window_code.png)
- [Basic Tkinter window output](screenshot_proofs/step_01_basic_window/step_01_c_basic_tkinter_window_output.png)

---

## Step 2: Added Number Buttons 1, 2, and 3

### What I did

In this step, I added the first three number buttons to the calculator.

I created:

- a `Frame` to hold the buttons,
- a function named `click_number(number)`,
- buttons for `1`, `2`, and `3`,
- click behavior that inserts the clicked number into the display.

### Code added in Step 2

```python
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
```

### What I tested

I ran:

```powershell
python .\calculator.py
```

Then I clicked:

```text
1
2
3
```

The display updated step by step:

```text
1
12
123
```

### What I learned

- `tk.Frame()` groups widgets together.
- `tk.Button()` creates a clickable button.
- `grid(row, column)` places widgets in a row-column layout.
- `command=` connects a button to a function.
- `lambda` helps pass a value to a function when a button is clicked.
- `display.insert(tk.END, number)` adds text to the end of the display.

### Screenshot proof

- [Code for buttons 1, 2, and 3](screenshot_proofs/step_02_number_buttons/step_02_a_code_for_buttons_1_2_3.png)
- [Terminal run from resubmission folder](screenshot_proofs/step_02_number_buttons/step_02_b_terminal_run_from_resubmission_folder.png)
- [Buttons visible in calculator window](screenshot_proofs/step_02_number_buttons/step_02_c_buttons_visible_in_window.png)
- [Display after clicking 1](screenshot_proofs/step_02_number_buttons/step_02_d_click_1_display_output.png)
- [Display after clicking 1 and 2](screenshot_proofs/step_02_number_buttons/step_02_e_click_1_2_display_output.png)
- [Display after clicking 1, 2, and 3](screenshot_proofs/step_02_number_buttons/step_02_f_click_1_2_3_display_output.png)

---

## Step 3: Added Remaining Number Buttons 4 to 9 and 0

### What I did

In this step, I completed the number button layout by adding buttons for `4`, `5`, `6`, `7`, `8`, `9`, and `0`.

I placed the buttons using `grid()` so that the calculator starts looking like a real calculator keypad.

### Code added in Step 3

```python
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
```

### What I tested

I ran:

```powershell
python .\calculator.py
```

Then I clicked all number buttons in order:

```text
1 2 3 4 5 6 7 8 9 0
```

The display showed:

```text
1234567890
```

### What I learned

- More buttons can be added by repeating the same basic `tk.Button()` pattern.
- `grid(row, column)` helps place buttons in a simple keypad layout.
- Each number button can call the same `click_number()` function with a different value.
- Repeating similar code manually helped me understand the pattern before making it shorter or cleaner.

### Screenshot proof

- [Code for all number buttons](screenshot_proofs/step_03_all_number_buttons/step_03_a_code_for_all_number_buttons.png)
- [All number buttons with `1234567890` displayed](screenshot_proofs/step_03_all_number_buttons/step_03_b_all_number_buttons_and_1234567890_output.png)
- [Terminal run from resubmission folder](screenshot_proofs/step_03_all_number_buttons/step_03_c_terminal_run_from_resubmission_folder.png)

---

## Step 4: Added Clear Button

### What I did

In this step, I added a clear button to reset the display.

I created:

- a function named `clear_display()`;
- a `C` button;
- click behavior that removes all text from the display.

### Code added in Step 4

```python
def clear_display():
    display.delete(0, tk.END)

clear_button = tk.Button(button_frame, text="C", width=5, height=2, command=clear_display)
clear_button.grid(row=3, column=0)
```

### What I tested

I clicked:

```text
1 2 3
```

The display showed:

```text
123
```

Then I clicked:

```text
C
```

The display became empty.

### What I learned

- `display.delete(0, tk.END)` deletes everything from the Entry field.
- A button can directly call a function through `command=clear_display`.
- The clear button is part of basic calculator state management because it resets the current input.

### Screenshot proof

- [Code for clear button](screenshot_proofs/step_04_clear_button/step_04_a_code_for_clear_button.png)
- [Before clear, display showing `123`](screenshot_proofs/step_04_clear_button/step_04_b_before_clear_display_123.png)
- [After clear, empty display](screenshot_proofs/step_04_clear_button/step_04_c_after_clear_empty_display.png)

---

## Step 5: Added Operator Buttons

### What I did

In this step, I added operator buttons for addition, subtraction, multiplication, and division.

I created:

- a function named `click_operator(operator)`;
- operator buttons for `+`, `-`, `*`, and `/`;
- click behavior that inserts the selected operator into the display.

At this stage, the calculator does not calculate yet. It only builds the expression text in the display.

### Code added in Step 5

```python
def click_operator(operator):
    display.insert(tk.END, operator)

plus_button = tk.Button(button_frame, text="+", width=5, height=2, command=lambda: click_operator("+"))
plus_button.grid(row=0, column=3)

minus_button = tk.Button(button_frame, text="-", width=5, height=2, command=lambda: click_operator("-"))
minus_button.grid(row=1, column=3)

multiply_button = tk.Button(button_frame, text="*", width=5, height=2, command=lambda: click_operator("*"))
multiply_button.grid(row=2, column=3)

divide_button = tk.Button(button_frame, text="/", width=5, height=2, command=lambda: click_operator("/"))
divide_button.grid(row=3, column=3)
```

### What I tested

I clicked:

```text
1 + 2
```

The display showed:

```text
1+2
```

### What I learned

- Operator buttons can work like number buttons at first by inserting symbols into the display.
- `lambda` is useful here because each operator button passes a different operator symbol.
- Building the expression first makes it easier to understand the next step, where the expression will be calculated.

### Screenshot proof

- [Code for `click_operator()` function](screenshot_proofs/step_05_operator_buttons/step_05_a_code_for_click_operator_function.png)
- [Code for operator buttons](screenshot_proofs/step_05_operator_buttons/step_05_b_code_for_operator_buttons.png)
- [Operator buttons visible in calculator window](screenshot_proofs/step_05_operator_buttons/step_05_c_operator_buttons_visible_in_window.png)
- [Expression `1+2` displayed](screenshot_proofs/step_05_operator_buttons/step_05_d_expression_1_plus_2_display_output.png)

---

## Step 6: Added Equals Button and Basic Calculation

### What I did

In this step, I added the equals button so that the expression typed into the display can be calculated.

I created:

- a function named `calculate_result()`;
- an equals button `=`;
- basic calculation using Python's `eval()` function;
- display replacement so that the expression is replaced by the final result.

At this stage, the calculator can calculate valid expressions. Error handling will be added separately in the next step.

### Code added in Step 6

```python
def calculate_result():
    expression = display.get()
    result = eval(expression)
    display.delete(0, tk.END)
    display.insert(tk.END, result)

equals_button = tk.Button(button_frame, text="=", width=5, height=2, command=calculate_result)
equals_button.grid(row=3, column=2)
```

### What I tested

I clicked:

```text
1 + 2 =
```

The display changed from:

```text
1+2
```

to:

```text
3
```

I also tested:

```text
7 * 10 =
```

The display changed from:

```text
7*10
```

to:

```text
70
```

### What I learned

- `display.get()` reads the current expression from the Entry field.
- `eval(expression)` can calculate a simple Python expression stored as text.
- `display.delete(0, tk.END)` clears the old expression.
- `display.insert(tk.END, result)` shows the result in the display.
- The equals button connects the calculation function to the GUI.

### Screenshot proof

- [Code for `calculate_result()` function](screenshot_proofs/step_06_equals_button/step_06_a_code_for_calculate_result_function.png)
- [Code for equals button](screenshot_proofs/step_06_equals_button/step_06_b_code_for_equals_button.png)
- [Equals button visible in calculator window](screenshot_proofs/step_06_equals_button/step_06_c_equals_button_visible_in_window.png)
- [Expression `1+2` before equals](screenshot_proofs/step_06_equals_button/step_06_d_expression_1_plus_2_before_equals.png)
- [Result `3` after equals](screenshot_proofs/step_06_equals_button/step_06_e_result_3_after_equals.png)
- [Expression `7*10` before equals](screenshot_proofs/step_06_equals_button/step_06_f_expression_7_multiply_10_before_equals.png)
- [Result `70` after equals](screenshot_proofs/step_06_equals_button/step_06_g_result_70_after_equals.png)

---

## Step 7: Added Simple Error Handling

### What I did

In this step, I updated the `calculate_result()` function so that the calculator does not crash when the expression is invalid.

I added:

- a `try` block for valid calculations;
- an `except` block for invalid expressions;
- an `Error` message in the display when calculation fails.

### Code updated in Step 7

```python
def calculate_result():
    expression = display.get()

    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
```

### What I tested

I tested a valid expression:

```text
1 + 3 =
```

The display changed from:

```text
1+3
```

to:

```text
4
```

I tested an invalid expression:

```text
1 * =
```

The display changed to:

```text
Error
```

I also tested division by zero:

```text
5 / 0 =
```

The display changed to:

```text
Error
```

### What I learned

- `try-except` helps prevent the program from crashing when something goes wrong.
- Invalid expressions can be handled by showing a simple message instead of stopping the app.
- Division by zero also creates an exception, so it can be handled by the same `except` block.
- This is a simple beginner-level way to handle calculator errors.

### Screenshot proof

- [Code for `try-except` error handling](screenshot_proofs/step_07_error_handling/step_07_a_code_for_try_except_error_handling.png)
- [Valid expression `1+3` before equals](screenshot_proofs/step_07_error_handling/step_07_b_valid_expression_1_plus_3_before_equals.png)
- [Valid result `4` after equals](screenshot_proofs/step_07_error_handling/step_07_c_valid_result_4_after_equals.png)
- [Invalid expression `1*` before equals](screenshot_proofs/step_07_error_handling/step_07_d_invalid_expression_1_multiply_before_equals.png)
- [Error after invalid expression](screenshot_proofs/step_07_error_handling/step_07_e_error_after_invalid_expression.png)
- [Divide-by-zero expression `5/0` before equals](screenshot_proofs/step_07_error_handling/step_07_f_divide_by_zero_expression_5_divide_0_before_equals.png)
- [Error after divide by zero](screenshot_proofs/step_07_error_handling/step_07_g_error_after_divide_by_zero.png)

---

## Step 8: Final Testing and Packaging

### What I did

In this final step, I tested the completed calculator after adding number buttons, operator buttons, the equals button, the clear button, and basic error handling.

I checked that the calculator can handle normal calculations as well as simple error situations.

### Final tests completed

| Test | Expression | Expected result |
| --- | --- | --- |
| Addition | `1+6` | `7` |
| Subtraction | `4-7` | `-3` |
| Multiplication | `7*45` | `315` |
| Division | `5/4` | `1.25` |
| Divide by zero | `5/0` | `Error` |
| Invalid expression | `5*` | `Error` |
| Clear button | Pressed `C` | Display cleared |

### What I learned

- Final testing is important before packaging the project.
- A calculator should be tested with all basic operators.
- Error cases are as important as successful calculation cases.
- Screenshot proofs help show the actual working process instead of only submitting code.

### Screenshot proof

- [Final app running](screenshot_proofs/step_08_final_testing/step_08_a_final_app_running.png)
- [Final code and app view](screenshot_proofs/step_08_final_testing/step_08_b_final_code_and_app_view.png)
- [Addition expression `1+6`](screenshot_proofs/step_08_final_testing/step_08_c_final_addition_expression_1_plus_6.png)
- [Addition result `7`](screenshot_proofs/step_08_final_testing/step_08_d_final_addition_result_7.png)
- [Subtraction expression `4-7`](screenshot_proofs/step_08_final_testing/step_08_e_final_subtraction_expression_4_minus_7.png)
- [Subtraction result `-3`](screenshot_proofs/step_08_final_testing/step_08_f_final_subtraction_result_minus_3.png)
- [Multiplication expression `7*45`](screenshot_proofs/step_08_final_testing/step_08_g_final_multiplication_expression_7_multiply_45.png)
- [Multiplication result `315`](screenshot_proofs/step_08_final_testing/step_08_h_final_multiplication_result_315.png)
- [Division expression `5/4`](screenshot_proofs/step_08_final_testing/step_08_i_final_division_expression_5_divide_4.png)
- [Division result `1.25`](screenshot_proofs/step_08_final_testing/step_08_j_final_division_result_1_point_25.png)
- [Divide-by-zero expression `5/0`](screenshot_proofs/step_08_final_testing/step_08_k_final_divide_by_zero_expression_5_divide_0.png)
- [Divide-by-zero error](screenshot_proofs/step_08_final_testing/step_08_l_final_divide_by_zero_error.png)
- [Invalid expression `5*`](screenshot_proofs/step_08_final_testing/step_08_m_final_invalid_expression_5_multiply.png)
- [Invalid expression error](screenshot_proofs/step_08_final_testing/step_08_n_final_invalid_expression_error.png)
- [Clear button final test](screenshot_proofs/step_08_final_testing/step_08_o_final_clear_button_test.png)

---

## Current Progress Checklist

- [x] Step 1: Create basic Tkinter window and display box.
- [x] Step 2: Add number buttons `1`, `2`, and `3`.
- [x] Step 3: Add remaining number buttons `4` to `9` and `0`.
- [x] Step 4: Add clear button.
- [x] Step 5: Add operator buttons.
- [x] Step 6: Add equals button and simple calculation.
- [x] Step 7: Add simple error handling.
- [x] Step 8: Final testing and packaging.
