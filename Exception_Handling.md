# Python Exception Handling — Student Notes

## 1. Errors and Exceptions: What's the Difference?

A program can have problems in different ways. **Error** is a general term for a problem in a program. An **exception** is a problem Python detects while executing a program and can potentially be handled.

### A. Syntax Error
A syntax error happens when we break Python's grammar/rules. Python cannot properly parse the code, so it cannot start normal execution of that code.

```python
if 10 > 5
    print("10 is greater")
```

**Why?** The colon (`:`) after the `if` condition is missing.

### B. Runtime Error / Exception
A runtime error occurs while the program is running. Python raises an exception when it encounters a problem during execution.

```python
a = 10
b = 0
print(a / b)
```

**Why?** Dividing by zero is not allowed. Python raises `ZeroDivisionError`.

### C. Logical Error
A logical error happens when the program runs without a syntax error or an unhandled exception, but the result is wrong because the programmer used incorrect logic.

```python
a = 10
b = 5
result = a - b  # Mistake: we intended addition
print("Addition:", result)
```

**Output:**
```text
Addition: 5
```
The program runs, but it gives the wrong result because subtraction was used instead of addition.

### Comparison

| Type | What happens? | Example | Can `try-except` handle it? |
|---|---|---|---|
| Syntax error | Python cannot parse the code correctly | Missing colon | No—fix the code syntax |
| Runtime error / exception | Problem occurs while executing | `10 / 0` | Yes, if the exception is caught |
| Logical error | Program runs but result/behavior is incorrect | Subtracting instead of adding | No—fix the program logic |

**Remember:** Exception handling mainly deals with runtime exceptions. It does not automatically fix syntax mistakes or incorrect logic.

---

## 2. What Is an Exception?

An **exception** is an event that occurs during program execution and interrupts the normal flow of instructions.

```python
print("Step 1")
result = 10 / 0
print("Step 2")
print("Step 3")
```

The program prints `Step 1`, then raises `ZeroDivisionError`. The remaining statements are skipped because the exception is not handled.

Exception handling helps us respond to such problems instead of allowing the program to stop unexpectedly.

---

## 3. Why Do We Need Exception Handling?

Suppose a calculator asks the user for a number and divides 100 by it. The user might enter `0` or text instead of a number. Without handling these cases, the program may terminate with an error.

Exception handling lets us:
- Display a useful message instead of an abrupt traceback.
- Handle unexpected or invalid input.
- Continue executing the program after a handled exception.
- Keep cleanup code running, such as closing files or releasing resources.

---

## 4. `try` and `except`

### Syntax

```python
try:
    # Code that might cause an exception
except:
    # Code that runs if an exception occurs
```

- `try`: Contains code that may cause an exception.
- `except`: Handles an exception raised inside the `try` block.

### Program 1: Handling Division by Zero

```python
try:
    a = 10
    b = 0
    result = a / b
    print(result)
except:
    print("Something went wrong!")

print("Program completed")
```

**Output:**
```text
Something went wrong!
Program completed
```

**What happens?** Python enters `try`, attempts division, encounters an exception, skips the rest of the `try` block, runs `except`, and then continues after the exception-handling structure.

> **Remember:** Once an exception occurs inside `try`, the remaining statements in that `try` block are skipped.

---

## 5. Common Python Exceptions

| Exception | When it occurs | Example |
|---|---|---|
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `ValueError` | Value is unsuitable for an operation | `int("hello")` |
| `TypeError` | Incompatible types used together | `"10" + 10` |
| `IndexError` | Accessing a list index that doesn't exist | `[10, 20][5]` |
| `NameError` | Using an undefined variable name | `print(total)` when `total` was never defined |
| `KeyError` | Accessing a missing dictionary key | `{"name": "A"}["age"]` |


### `ValueError` vs `TypeError`
- **TypeError:** The kind/type of data is not suitable for the operation. Example: adding a string and an integer (`"10" + 10`).
- **ValueError:** The type is acceptable, but the particular value is not. Example: converting the text `"hello"` to an integer (`int("hello")`).

---

## 6. Handling Specific Exceptions

Instead of a generic `except`, we can specify which exception we want to handle.

```python
try:
    # Risky code
except ValueError:
    # Handle ValueError
except ZeroDivisionError:
    # Handle ZeroDivisionError
```

### Program 2: Division Calculator

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
```

**Sample outcomes:**
- Input `5` → `Result: 20.0`
- Input `0` → `You cannot divide by zero`
- Input `hello` → `Please enter a valid number`

**Important:** Python executes only the matching `except` block. If no exception occurs, all `except` blocks are skipped.

---

## 7. Multiple Statements Inside `try`

An exception can occur at any statement inside `try`. Once it occurs, the remaining statements in that `try` block are skipped.

### Program 3: Find the First Exception

```python
try:
    print("Step 1")
    x = int("hello")
    print("Step 2")
    y = 10 / 0
    print("Step 3")
except ValueError:
    print("Value Error Occurred")
except ZeroDivisionError:
    print("Division Error Occurred")

print("Program End")
```

**Output:**
```text
Step 1
Value Error Occurred
Program End
```

**Explanation:** `int("hello")` raises `ValueError` first. `Step 2`, the division, and `Step 3` are never reached. The `ValueError` handler runs, then execution continues at `Program End`.

> **Exam tip:** Identify the first statement that raises an exception. All later statements in that same `try` block are skipped.

---

## 8. The `else` Block

The `else` block runs **only if no exception occurs** in the `try` block.

### Syntax

```python
try:
    # Risky code
except:
    # Runs if an exception occurs
else:
    # Runs only if there was no exception
```

### Program 4: Using `else`

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
    print("Calculation successful")
```

- Input `5`: prints the result and `Calculation successful`.
- Input `0`: prints `Cannot divide by zero`; `else` is skipped.
- Input `abc`: prints `Invalid input`; `else` is skipped.

| Situation | `try` | `except` | `else` |
|---|---|---|---|
| No exception | Executes | Skipped | Executes |
| Exception occurs | Executes until error | Matching handler executes | Skipped |

---

## 9. The `finally` Block

The `finally` block executes after the `try`/`except` structure finishes in normal exception-handling flow, whether an exception occurred or not. It is often used for cleanup—closing files, database connections, or releasing resources.

### Syntax

```python
try:
    # Risky code
except:
    # Error handling
finally:
    # Cleanup/final code
```

### Program 5: Using `finally`

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Program execution completed")
```

- Input `5`: result, success path, then finally message.
- Input `0`: zero-division message, then finally message.
- Input `abc`: invalid-input message, then finally message.

### `try`, `except`, `else`, `finally` summary

| Block | When it executes |
|---|---|
| `try` | First; runs until an exception or completion |
| `except` | When a matching exception occurs |
| `else` | When no exception occurs in `try` |
| `finally` | At the end of the exception-handling flow, regardless of whether an exception occurred |

---

## 10. The `raise` Keyword

The `raise` keyword lets the programmer deliberately raise an exception when a condition violates a rule.

### Syntax

```python
raise ExceptionType("Error message")
```

### Program 6: Age Validation

```python
age = 15

if age < 18:
    raise ValueError("You must be 18 or older")

print("Access granted")
```

This raises `ValueError` because the age is below 18. Since the exception is not handled here, normal execution stops and `Access granted` is not printed.

`raise` is useful for enforcing rules, such as:
- Age must meet a minimum requirement.
- Withdrawal cannot exceed the account balance.
- Marks must be between 0 and 100.
- Quantity cannot be negative.

---

## 11. Handling an Exception Raised by `raise`

We can raise an exception and catch it using `try` and `except`.

### Program 7: Age Validation with Handling

```python
age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible")
except ValueError as e:
    print("Error:", e)

print("Program completed")
```

**Output:**
```text
Error: Age must be 18 or above
Program completed
```

In `except ValueError as e`, the variable `e` refers to the exception object, so printing it displays its error message.

---

## 12. User-Defined (Custom) Exceptions

Python allows us to create our own exception types. A custom exception is usually created by defining a class that inherits from Python's built-in `Exception` class.

### Syntax

```python
class MyCustomException(Exception):
    pass
```

- `class` defines a new class.
- `MyCustomException` is the exception's name.
- `Exception` is the parent class.
- `pass` means no additional implementation is added for now.

### Program 8: Creating a Custom Exception

```python
class InvalidAgeError(Exception):
    pass



try:
    age = 15
    if age < 18:
        raise InvalidAgeError("You must be 18 or older")
    print("Eligible")
except InvalidAgeError as e:
    print("Error:", e)

print("Program completed")
```

**Output:**
```text
Error: You must be 18 or older
Program completed
```

Custom exceptions are useful for application-specific problems, such as `InvalidAgeError`, `InsufficientBalanceError`, `InvalidMarksError`, or `UserNotFoundError`.

---

## 13. Real-World Example: Bank Withdrawal

This program combines custom exceptions, `raise`, `except`, and `finally`.

### Program 9: Bank Transaction

```python
class InsufficientBalanceError(Exception):
    pass



balance = 5000
withdrawal = 7000

try:
    if withdrawal > balance:
        raise InsufficientBalanceError("Insufficient bank balance")

    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Transaction failed:", e)

finally:
    print("Thank you for using our bank")
```

**Output:**
```text
Transaction failed: Insufficient bank balance
Thank you for using our bank
```

**Flow:** The withdrawal exceeds the balance → custom exception is raised → normal `try` flow stops → matching `except` handles it → `finally` runs.

---

## 14. Complete Example: Safe Division Calculator

This example combines several concepts.

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Division result:", result)
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError:
    print("Second number cannot be zero")
else:
    print("Calculation successful")
finally:
    print("Program execution completed")
```

### Test it with these inputs

| First number | Second number | Expected behavior |
|---:|---:|---|
| 20 | 5 | Result: 4.0; success message |
| 10 | 0 | Zero-division message; finally message |
| `abc` | 5 | Value error message; finally message |
| 20 | `xyz` | Value error message; finally message |
| -20 | 5 | Result: -4.0; success message |

---

## 15. Important Rules to Remember

1. A **syntax error** means the code breaks Python grammar/rules.
2. A **runtime error/exception** happens during execution; it can be handled with `try-except` if the matching handler is present.
3. A **logical error** means the program runs but produces incorrect behavior/results.
4. Code inside `try` runs until an exception occurs or the block completes.
5. When an exception occurs, the rest of that `try` block is skipped.
6. Only the matching `except` block executes.
7. `else` executes only if there is no exception.
8. `finally` executes at the end of the exception-handling flow, whether an exception occurred or not.
9. `raise` manually triggers an exception.
10. Custom exceptions are created by inheriting from `Exception`.
11. A `try` block protects only the code inside it—not statements outside it.
12. Prefer specific exception handlers (e.g., `ValueError`, `ZeroDivisionError`) rather than a bare `except` when possible.

---

## 16. Common Mistakes

### Mistake 1: Risky code outside `try`

```python
result = 10 / 0

try:
    print(result)
except ZeroDivisionError:
    print("Error")
```

The division occurs before Python enters `try`, so this handler cannot catch it.

### Mistake 2: Expecting `else` after an exception

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```

Output is `Error`. The `else` block is skipped because an exception occurred.

### Mistake 3: Expecting all `except` blocks to execute

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Zero division")
except ValueError:
    print("Value error")
```

Only `Zero division` prints. Python executes the matching handler, not every handler.

### Mistake 4: Expecting statements after `raise` to run

```python
raise ValueError("Invalid")
print("Hello")
```

`print("Hello")` is not executed because the unhandled exception stops normal flow.

---

## 17. Practice Questions

Try these yourself before checking any solution.

### Q1. Predict the output

```python
try:
    print("A")
    x = 10 / 0
    print("B")
except ZeroDivisionError:
    print("C")
print("D")
```

### Q2. Predict the output

```python
try:
    x = int("50")
    print(x)
except ValueError:
    print("Error")
else:
    print("Success")
finally:
    print("End")
```

### Q3. Predict the output

```python
try:
    x = int("abc")
    print("A")
except ValueError:
    print("B")
else:
    print("C")
finally:
    print("D")
```

### Q4. Predict the output

```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("Done")
```

### Q5. Predict the output

```python
try:
    x = 10
    y = 0
    print(x / y)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero Division")
else:
    print("Success")
finally:
    print("Finished")
```

### Q6. Write a program

1. Accept a number from the user.
2. Convert it to an integer.
3. Divide 100 by the number.
4. Handle invalid input using `ValueError`.
5. Handle division by zero using `ZeroDivisionError`.
6. Print `Calculation completed` using `finally`.

### Q7. Write a program

Write a driving-license eligibility program:
- Accept the user's age.
- If age is less than 18, raise a `ValueError`.
- Handle the exception and print an appropriate message.
- Otherwise, display `Eligible for driving license`.

### Q8. Write a program

Create a custom exception named `InsufficientBalanceError`:
- Set `balance = 10000`.
- Accept a withdrawal amount.
- Raise your custom exception if withdrawal exceeds the balance.
- Otherwise deduct the amount and print the remaining balance.
- Handle your custom exception with `except`.

### Q9. Write a program

Create a marks-validation program:
- Accept marks from the user.
- Raise `ValueError` if marks are below 0 or above 100.
- Print marks if valid.
- Handle the exception with a meaningful message.

### Q10. Predict the exact output

```python
try:
    a = int("10")
    b = int("hello")
    c = 10 / 0
except ZeroDivisionError:
    print("Zero")
except ValueError:
    print("Value")
else:
    print("Else")
finally:
    print("Finally")
print("End")
```
Explain why that output appears.

---

## Quick Revision Cheat Sheet

| Keyword | Purpose |
|---|---|
| `try` | Contains code that may raise an exception |
| `except` | Handles a matching exception |
| `else` | Runs if no exception occurs in `try` |
| `finally` | Runs at the end of the exception-handling flow |
| `raise` | Manually raises an exception |
| `Exception` | Base class used to define custom exceptions |

### Basic structure

```python
try:
    risky_code()
except ValueError:
    handle_error()
else:
    success_message()
finally:
    cleanup()
```

**Before your programming test, make sure you can:**
- Write a basic `try-except` block without looking at notes.
- Identify common exception types from code.
- Predict output involving `try`, `except`, `else`, and `finally`.
- Use `raise` to validate input.
- Create and handle a simple custom exception.
