# Python Decorators – Student Notes

## 1. What is a Function?

A **function** is a reusable block of code that performs a particular task.

```python
def greet():
    print("Hello!")

greet()
```

**Output:**
```text
Hello!
```

Functions help us avoid writing the same code repeatedly and make programs easier to organize.

---

## 2. Functions are Objects in Python

In Python, functions can be treated like other objects. We can assign a function to another variable and call it using that variable.

```python
def greet():
    print("Hello!")

message = greet
message()
```

**Output:**
```text
Hello!
```

Here, `message` refers to the same function as `greet`. Notice that we use `greet` without parentheses when assigning it. Writing `greet()` would call the function immediately.

---

## 3. Passing a Function to Another Function

A function can be passed as an argument to another function.

```python
def greet():
    print("Hello!")

def call_function(func):
    func()

call_function(greet)
```

**Output:**
```text
Hello!
```

### How does this work?

1. `greet` is passed to `call_function` as an argument.
2. Inside `call_function`, the parameter `func` refers to the passed function.
3. `func()` calls that function.

Remember: we pass `greet`, not `greet()`, because we want to pass the function itself—not execute it at that moment.

---

## 4. Nested Functions

A function can be defined inside another function. Such a function is called a **nested function** (or inner function).

```python
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()
```

**Output:**
```text
Outer function
Inner function
```

The `inner()` function is defined inside `outer()`. In this example, it is called from within the outer function.

---

## 5. Returning a Function

A function can return another function.

```python
def outer():
    def inner():
        print("Inner function called")

    return inner

result = outer()
result()
```

**Output:**
```text
Inner function called
```

### Understand the steps

- `outer()` runs and defines `inner()`.
- `outer()` returns the function `inner` (without calling it).
- The returned function is stored in `result`.
- `result()` calls the returned function.

---

## 6. What is a Decorator?

A **decorator** is a function that takes another function, adds some extra behavior to it, and returns a function—without needing to change the original function's code.

For example, imagine we have a function that displays a welcome message. We want to display a line before and after that message too. A decorator lets us add this behavior around the original function.

---

## 7. Creating Our First Decorator (Without `@` Syntax)

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


def greet():
    print("Hello!")

modified_greet = my_decorator(greet)
modified_greet()
```

**Output:**
```text
Before function
Hello!
After function
```

### Explanation

- `my_decorator(func)` receives the original function (`greet`).
- `wrapper()` is the new function that adds extra steps.
- `func()` calls the original function.
- `return wrapper` returns the wrapper function.
- `modified_greet()` calls the returned wrapper, so the added statements and the original function run.

### Flow of execution

```text
modified_greet()
       |
       v
    wrapper()
       |
       +--> Print "Before function"
       +--> Call original greet()
       |       +--> Print "Hello!"
       +--> Print "After function"
```

---

## 8. Using the `@` Decorator Syntax

Python provides a shorter way to apply a decorator using `@`.

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def greet():
    print("Hello!")

greet()
```

**Output:**
```text
Before function
Hello!
After function
```

This line:

```python
@my_decorator
```

is equivalent to:

```python
greet = my_decorator(greet)
```

Python applies the decorator to the function and replaces the name `greet` with the function returned by the decorator.

---

## 9. Example: Decorator for Displaying a Message

We can use a decorator to display a message before and after a function executes.

```python
def announcement(func):
    def wrapper():
        print("Program is starting")
        func()
        print("Program has finished")
    return wrapper

@announcement
def show_marks():
    print("Marks: 85")

show_marks()
```

**Output:**
```text
Program is starting
Marks: 85
Program has finished
```

---

## 10. Decorators with Function Arguments

So far, our wrapper functions did not accept any arguments. What if the original function accepts arguments?

We need to pass those arguments to the wrapper and then forward them to the original function.

```python
def my_decorator(func):
    def wrapper(name):
        print("Function is being called")
        func(name)
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Aarav")
```

**Output:**
```text
Function is being called
Hello Aarav
```

Here, `wrapper(name)` accepts the argument and passes it to the original function using `func(name)`.

---

## 11. Decorator with a Return Value

If the original function returns a value, the wrapper should return that value too, so it is not lost.

```python
def my_decorator(func):
    def wrapper(a, b):
        print("Calculating...")
        result = func(a, b)
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

answer = add(10, 20)
print("Result:", answer)
```

**Output:**
```text
Calculating...
Result: 30
```

### Key point

The wrapper calls the original function, stores its returned value, and returns that value to the caller.

---

## 12. Practical Example: Measuring the Execution of a Function (Simple Version)

A decorator can run code before and after a function. For example, it can print a message indicating that a task is being performed.

```python
def task_info(func):
    def wrapper():
        print("Task started")
        func()
        print("Task completed")
    return wrapper

@task_info
def download_file():
    print("Downloading file...")

download_file()
```

**Output:**
```text
Task started
Downloading file...
Task completed
```

This illustrates how decorators can be useful for adding common behavior to functions.

---

## 13. Important Points to Remember

- A decorator is a function that takes another function and returns a function with added behavior.
- A decorator can add behavior before and/or after the original function runs.
- The original function's code does not need to be modified to add the decorator behavior.
- `wrapper()` is commonly used as the inner function name, but it can have another name.
- `@decorator_name` is the shorter syntax for applying a decorator.
- The wrapper must accept the arguments required by the decorated function in the examples shown.
- If the decorated function returns a value, the wrapper should return it too when we want to preserve that result.

---

## 14. Common Mistakes

### Mistake 1: Calling the function instead of passing it

Incorrect:
```python
modified = my_decorator(greet())
```

Correct:
```python
modified = my_decorator(greet)
```

`greet()` executes the function immediately. `greet` passes the function itself to the decorator.

### Mistake 2: Forgetting to return the wrapper

Incorrect:
```python
def my_decorator(func):
    def wrapper():
        func()
```

Correct:
```python
def my_decorator(func):
    def wrapper():
        func()
    return wrapper
```

Without `return wrapper`, the decorator does not return the function that should be called.

### Mistake 3: Forgetting to call the original function inside wrapper

If `func()` is not called inside `wrapper()`, the original function's code will not execute.

### Mistake 4: Forgetting to return the original result

If the original function returns a value and the wrapper does not return it, the decorated function may return `None` instead of the expected result.

---

# Practice Programs

Try solving these questions yourself. Write the code, run it, and verify the output. Use comments to explain the logic of your program.

## Level 1 – Basics

**1. Decorator Before and After**  
Create a decorator named `message_decorator` that prints `Starting execution` before the original function and `Execution completed` after it. Apply it to a function named `display` that prints `Welcome to Python`.

**2. Decorator for Student Details**  
Create a decorator that prints `Student information` before a decorated function. The function should print a student's name and division.

**3. Apply a Decorator Without `@`**  
Create a decorator named `simple_decorator`. Apply it to a function named `show_message` without using the `@` syntax. Call the decorated function and observe the output.

**4. Predict the Output**  
Study the code and write the exact output before running it.

```python
def decorator(func):
    def wrapper():
        print("First")
        func()
        print("Last")
    return wrapper

@decorator
def display():
    print("Middle")

display()
```

## Level 2 – Arguments and Return Values

**5. Decorator with a Name Argument**  
Create a decorator that prints `Greeting started`. Decorate a function that accepts a person's name and prints `Hello` followed by that name.

**6. Decorator for Addition**  
Create a decorator that prints `Addition is being performed`. Apply it to an `add(a, b)` function that returns the sum. Print the returned result.

**7. Decorator for Multiplication**  
Create a decorator that prints `Multiplication is being performed` before calling the original function. Decorate a `multiply(a, b)` function and return the product.

**8. Predict the Output**  
Write the output of this code and explain when each function is called.

```python
def decorator(func):
    def wrapper(x):
        print("Before")
        func(x)
    return wrapper

@decorator
def show(x):
    print(x * 2)

show(5)
```

## Level 3 – Understanding and Application

**9. Decorator for Marks**  
Create a decorator that prints `Checking result` before a function. The function should accept marks and display whether the student has passed (marks 40 or above) or failed.

**10. Decorator for Even/Odd**  
Create a decorator that prints `Number checking started`. Decorate a function that accepts an integer and displays whether it is even or odd.

**11. Decorator for a Calculator**  
Create a decorator that displays `Calculator started` before the function and `Calculator finished` after it. Decorate a function that accepts two numbers and displays their sum, difference, and product.

**12. Decorator for Login Message**  
Create a decorator that prints `Verifying user` before a decorated function. Create a function that accepts a username and prints `Welcome, <username>`.

**13. Decorator with a Return Value**  
Create a decorator for a function that calculates the square of a number. The decorator should print `Square calculation started` and preserve the returned square value. Print the final result.

**14. Create Your Own Decorator**  
Write your own decorator. Apply it to any function of your choice. Your decorator must print at least one message before the original function and one message after it. The decorated function must accept at least one argument.

---

# Quick Revision

| Term | Meaning |
|---|---|
| Function | Reusable block of code that performs a task |
| Function as object | A function can be assigned to a variable or passed to another function |
| Nested function | Function defined inside another function |
| Decorator | Function that takes another function and returns a modified/wrapped function |
| `wrapper()` | Inner function commonly used to add behavior around the original function |
| `@decorator` | Syntax for applying a decorator to a function |
| `func()` | Calls the original function from inside the wrapper |
| `return wrapper` | Returns the wrapper function from the decorator |

**Remember:** A decorator adds functionality to an existing function without requiring us to change the original function's code.
