# 🔢 Module 3: Variables, Expressions, & Data Types

> **Course:** Programming for Everybody (Getting Started with Python) — University of Michigan  
> **Instructor:** Dr. Charles Severance ("Dr. Chuck")  
> **Student & Maintainer:** [Abid Zada](https://github.com/Abidzada1688)

---

## 👨‍🏫 1. Instructor Core Concepts (Dr. Chuck)

### 🔹 Constants
Constants are fixed values that do not change during program execution.
* **Numeric Constants:** `123`, `98.6`, `-45`
* **String Constants:** `"Hello World"`, `'Python for Everybody'` *(enclosed in single or double quotes)*

### 🔹 Variables & Assignment Statements
A **variable** is a named memory location where a programmer can store data and later retrieve or update it.
* The assignment operator (`=`) is read as **"assign/store value on the right into the variable on the left"**.
* Values in variables can overwrite previous values.

```python
x = 12.2    # Store 12.2 in memory location named x
x = 14.0    # Overwrite previous value with 14.0
```

###  User Input and Type Conversion
* `input()` pauses program execution and prompts the user to enter text.
* The `input()` function **always returns a string**, even if the user enters digits.
* To perform calculations on user input, explicitly convert the string to a numeric type using `int()` or `float()`.

---