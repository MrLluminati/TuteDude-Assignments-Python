# Assignment 6 Resubmission: Tkinter Calculator

## Resubmission Reason

The first submission was rejected because it appeared too polished and did not clearly show my learning process. I rebuilt the calculator step by step with screenshots. After the later mentor review, I received one more correction: the earlier calculation shortcut was not allowed, so I refactored the calculator to use manual arithmetic logic.

## AI Usage Note

AI assistance was used only for conceptual guidance, debugging support, README structuring, and screenshot organization. The final corrected logic was rebuilt incrementally to understand Tkinter event handling, state variables, and arithmetic flow.

## Current Files

| File / Folder | Purpose |
| --- | --- |
| [`calculator.py`](calculator.py) | Final Tkinter calculator implementation using manual arithmetic logic. |
| [`screenshot_proofs/`](screenshot_proofs/) | Step-wise proof screenshots showing learning, testing, and corrections. |

---

## Step Summary

| Step | Work Completed | Screenshot Folder |
| --- | --- | --- |
| Step 1 | Basic Tkinter window and display box | [`step_01_basic_window`](screenshot_proofs/step_01_basic_window/) |
| Step 2 | Added number buttons 1, 2, and 3 | [`step_02_number_buttons`](screenshot_proofs/step_02_number_buttons/) |
| Step 3 | Added remaining number buttons 4 to 9 and 0 | [`step_03_all_number_buttons`](screenshot_proofs/step_03_all_number_buttons/) |
| Step 4 | Added clear button | [`step_04_clear_button`](screenshot_proofs/step_04_clear_button/) |
| Step 5 | Added operator buttons | [`step_05_operator_buttons`](screenshot_proofs/step_05_operator_buttons/) |
| Step 6 | Added equals button and first calculation attempt | [`step_06_equals_button`](screenshot_proofs/step_06_equals_button/) |
| Step 7 | Added simple error handling | [`step_07_error_handling`](screenshot_proofs/step_07_error_handling/) |
| Step 8 | Final testing of first resubmission | [`step_08_final_testing`](screenshot_proofs/step_08_final_testing/) |
| Step 9 | Removed the disallowed calculation shortcut and added manual arithmetic logic | [`step_09_manual_arithmetic_no_eval`](screenshot_proofs/step_09_manual_arithmetic_no_eval/) |

---

## Step 9: Manual Arithmetic Fix

### Why this step was needed

The mentor specifically stated that the previous calculation approach was not assignment-compliant. The calculator had to be refactored so that it manually stores the first number, selected operator, and second number, and then performs the calculation based on the selected operator.

### What I changed

I added three state variables:

```python
first_number = ""
operator = ""
second_number = ""
```

The corrected calculator now works like this:

- number button clicks are stored in `first_number` before an operator is selected;
- number button clicks are stored in `second_number` after an operator is selected;
- operator button clicks store the selected operator;
- the equals button calculates using normal conditional logic;
- divide-by-zero and incomplete expressions show `Error`;
- the corrected version does not use the forbidden shortcut.

### Manual arithmetic logic

```python
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
```

### Tests completed

| Test | Expression | Result |
| --- | --- | --- |
| Addition | `1+6` | `7.0` |
| Subtraction | `4-7` | `-3.0` |
| Multiplication | `7*45` | `315.0` |
| Division | `5/4` | `1.25` |
| Divide by zero | `5/0` | `Error` |
| Invalid expression | `5*` | `Error` |

### Screenshot proof

- [Code showing global variables and number handling](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_a_code_global_variables_and_click_number.png)
- [Code showing clear/operator logic and start of calculation](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_b_code_clear_operator_and_start_of_calculate_result.png)
- [Code showing manual calculation logic](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_c_code_manual_calculate_result_no_eval.png)
- [Addition expression `1+6`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_d_valid_addition_expression_1_plus_6.png)
- [Addition result `7.0`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_e_valid_addition_result_7_point_0.png)
- [Subtraction expression `4-7`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_f_valid_subtraction_expression_4_minus_7.png)
- [Subtraction result `-3.0`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_g_valid_subtraction_result_minus_3_point_0.png)
- [Multiplication expression `7*45`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_h_valid_multiplication_expression_7_multiply_45.png)
- [Multiplication result `315.0`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_i_valid_multiplication_result_315_point_0.png)
- [Division expression `5/4`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_j_valid_division_expression_5_divide_4.png)
- [Division result `1.25`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_k_valid_division_result_1_point_25.png)
- [Divide-by-zero expression `5/0`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_l_divide_by_zero_expression_5_divide_0.png)
- [Divide-by-zero error](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_m_divide_by_zero_error.png)
- [Invalid expression `5*`](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_n_invalid_expression_5_multiply.png)
- [Invalid expression error](screenshot_proofs/step_09_manual_arithmetic_no_eval/step_09_o_invalid_expression_error.png)

---

## Current Progress Checklist

- [x] Step 1: Create basic Tkinter window and display box.
- [x] Step 2: Add number buttons.
- [x] Step 3: Add all number buttons.
- [x] Step 4: Add clear button.
- [x] Step 5: Add operator buttons.
- [x] Step 6: Add equals button.
- [x] Step 7: Add simple error handling.
- [x] Step 8: Complete first final testing.
- [x] Step 9: Remove disallowed calculation shortcut and implement manual arithmetic logic.
