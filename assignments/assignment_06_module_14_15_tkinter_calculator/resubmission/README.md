## Resubmission Learning Log

### Step 1: Basic Tkinter Window and Display Box

In this step, I started rebuilding the calculator from the beginning in a simple beginner-friendly style.

What I tried first:
- Opened the Assignment 6 folder.
- Created a new file named `calculator.py`.
- Started writing a basic Tkinter program.
- Made a few command-line and typing mistakes while working.

Mistakes/debugging during this step:
- I accidentally typed `notpad` instead of `notepad`.
- I accidentally typed `import tkinter as tk` directly into PowerShell instead of writing it inside the Python file.
- I ran `python .` instead of running the actual file using `python .\calculator.py`.
- I made a typo by writing `windo.geometry(...)` instead of `window.geometry(...)`, which caused a `NameError`.

How I fixed it:
- I corrected the file command.
- I moved the Python code into `calculator.py`.
- I ran the correct file using `python .\calculator.py`.
- I corrected `windo` to `window`.

Code completed in this step:

```python
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

display = tk.Entry(window, width=25, font=("Arial", 18), justify="right")
display.pack(pady=20)

window.mainloop()

What I learned:

tk.Tk() creates the main application window.
window.title() sets the title of the window.
window.geometry() sets the size of the window.
tk.Entry() creates an input/display box.
pack() places the widget inside the window.
mainloop() keeps the Tkinter window running.

Screenshot proof:

screenshot_proofs/step_01_basic_window/step_01_a_terminal_mistakes_and_nameerror.png
screenshot_proofs/step_01_basic_window/step_01_b_corrected_basic_window_code.png
screenshot_proofs/step_01_basic_window/step_01_c_basic_tkinter_window_output.png

