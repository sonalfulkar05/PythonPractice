# Async IO – Practice Programming Questions

## Instructions

- Write the Python program for each question.
- Use `async def` to define asynchronous functions wherever required.
- Use `await` to wait for asynchronous operations.
- Use `asyncio.sleep()` wherever a delay is specified.
- Use `asyncio.gather()` wherever multiple tasks are required to execute concurrently.
- Use `asyncio.run(main())` to execute your program.
- Add comments explaining the logic used in your code.

---

## Level 1 – Basic Async IO Programs

### Q1. Hello and Welcome

Write an asynchronous function that prints `"Hello"`, waits for 2 seconds, and then prints `"Welcome to Python"`.

### Q2. Number Sequence with Delay

Write an asynchronous function to print numbers from 1 to 5. The program should wait for 1 second between printing each number.

### Q3. Countdown

Write an asynchronous function that prints numbers from 5 to 1 with a delay of 1 second between each number. After completing the countdown, print `"Time's Up!"`.

### Q4. Student Welcome Message

Write an asynchronous function that accepts a student's name, waits for 2 seconds, and then prints:

`Welcome, [name]!`

Call the function for any three student names.

---

## Level 2 – Async Functions and Return Values

### Q5. Square of a Number

Create an asynchronous function `square(n)` that waits for 2 seconds and returns the square of the given number.

Call the function for a number and print the returned result.

### Q6. Cube of a Number

Create an asynchronous function `cube(n)` that returns the cube of a number after waiting for 2 seconds.

Test the function with at least three different numbers.

### Q7. Addition Using Async Function

Create an asynchronous function `add(a, b)` that waits for 1 second and returns the sum of two numbers.

Call the function and print the result.

### Q8. Even or Odd

Create an asynchronous function that accepts a number, waits for 1 second, and returns whether the number is even or odd.

Example:

- Input: `8`
- Output: `8 is Even`

---

## Level 3 – Using `asyncio.gather()`

### Q9. Run Two Welcome Functions Concurrently

Create two asynchronous functions that print different messages. Run both functions together using `asyncio.gather()`.

Each function should wait for 2 seconds before printing its final message.

### Q10. Calculate Three Squares Concurrently

Create an asynchronous function `square(n)` that waits for 2 seconds and returns the square of a number.

Use `asyncio.gather()` to calculate the squares of 2, 3, and 4 concurrently. Print all the results in a list.

**Expected Output:**

```text
[4, 9, 16]
```

### Q11. Calculate Three Cubes Concurrently

Create an asynchronous function to calculate the cube of a number.

Use `asyncio.gather()` to calculate the cubes of 2, 3, and 5 concurrently and display the results.

**Expected Output:**

```text
[8, 27, 125]
```

### Q12. Multiple Student Welcome Messages

Create an asynchronous function that accepts a student's name, waits for 2 seconds, and returns a welcome message.

Use `asyncio.gather()` to execute the function for three students concurrently and print all returned messages.

---

## Level 4 – Logic Building and Output

### Q13. Multiplication Tables Concurrently

Create an asynchronous function `table(n)` that prints the multiplication table of a given number from 1 to 10.

Use `asyncio.gather()` to print the tables of 2, 3, and 5 concurrently.

### Q14. Predict and Verify the Output

Study the following program and write down the expected output. Then execute the program and verify your answer.

```python
import asyncio

async def task1():
    print("Task 1 Started")
    await asyncio.sleep(2)
    print("Task 1 Completed")

async def task2():
    print("Task 2 Started")
    await asyncio.sleep(1)
    print("Task 2 Completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

Answer the following:

1. Which statements are printed first?
2. Which task completes first?
3. Why doesn't Task 1 block Task 2 while waiting?
4. Approximately how long does the program take to finish?

### Q15. Multiple Delayed Tasks

Create three asynchronous functions:

- Task 1 waits for 3 seconds and returns `"Task 1 Done"`.
- Task 2 waits for 1 second and returns `"Task 2 Done"`.
- Task 3 waits for 2 seconds and returns `"Task 3 Done"`.

Execute all three using `asyncio.gather()` and print the returned list.

Observe the order of results in the list. Does it depend on which task completes first?
