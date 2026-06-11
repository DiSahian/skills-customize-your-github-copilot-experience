# 📘 Assignment: Functions and Modules

## 🎯 Objective

Learn how to organize Python code using reusable functions and modules, and practice importing helper code from a separate file.

## 📝 Tasks

### 🛠️ Define reusable functions

#### Description
Write helper functions in a new module file called `helpers.py`.

#### Requirements
Completed program should:

- Define a function `greet_user(name)` that returns a greeting string.
- Define a function `calculate_rectangle_area(length, width)` that returns the area of a rectangle.
- Define a function `is_palindrome(text)` that returns `True` when the text reads the same forwards and backwards, ignoring spaces and punctuation.

### 🛠️ Create and import a module

#### Description
Keep your helper functions in `helpers.py` and import them into `starter-code.py`.

#### Requirements
Completed program should:

- Create `helpers.py` containing the three helper functions.
- Import the functions from `helpers.py` into `starter-code.py`.
- Use the imported functions in the main program.

### 🛠️ Use module functions in the main program

#### Description
Interact with the user and call your imported helper functions to show results.

#### Requirements
Completed program should:

- Ask the user for their name and print a greeting using `greet_user()`.
- Ask the user for rectangle dimensions and print the area using `calculate_rectangle_area()`.
- Ask the user for a word or phrase and print whether it is a palindrome using `is_palindrome()`.
