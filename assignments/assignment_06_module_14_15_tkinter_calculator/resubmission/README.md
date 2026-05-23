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
| `calculator.py` | Beginner-level Tkinter calculator rebuilt step by step. |
| `screenshot_proofs/` | Screenshots showing progress, mistakes, fixes, and outputs. |

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

- `screenshot_proofs/step_01_basic_window/step_01_a_terminal_mistakes_and_nameerror.png`
- `screenshot_proofs/step_01_basic_window/step_01_b_corrected_basic_window_code.png`
- `screenshot_proofs/step_01_basic_window/step_01_c_basic_tkinter_window_output.png`

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

- `screenshot_proofs/step_02_number_buttons/step_02_a_code_for_buttons_1_2_3.png`
- `screenshot_proofs/step_02_number_buttons/step_02_b_terminal_run_from_resubmission_folder.png`
- `screenshot_proofs/step_02_number_buttons/step_02_c_buttons_visible_in_window.png`
- `screenshot_proofs/step_02_number_buttons/step_02_d_click_1_display_output.png`
- `screenshot_proofs/step_02_number_buttons/step_02_e_click_1_2_display_output.png`
- `screenshot_proofs/step_02_number_buttons/step_02_f_click_1_2_3_display_output.png`

---

## Current Progress Checklist

- [x] Step 1: Create basic Tkinter window and display box.
- [x] Step 2: Add number buttons `1`, `2`, and `3`.
- [ ] Step 3: Add remaining number buttons `4` to `9` and `0`.
- [ ] Step 4: Add clear button.
- [ ] Step 5: Add operator buttons.
- [ ] Step 6: Add equals button and simple calculation.
- [ ] Step 7: Add simple error handling.
- [ ] Step 8: Final testing and packaging.