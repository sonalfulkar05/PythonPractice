# Python Async IO — Student Notes

## 1. What Is Synchronous Execution?

In **synchronous execution**, tasks are performed one after another. A task must finish before the next task starts.

Example: if three independent tasks each take 2 seconds, doing them one after another takes approximately 6 seconds.

## 2. What Is Asynchronous Execution?

**Asynchronous execution** allows a program to make progress on other tasks while one task is waiting for an operation to finish.

For example, a program may need to wait for a network response. Instead of staying idle during the wait, it can let another task run.

Async IO is particularly useful for operations involving waiting, such as network communication or other input/output (I/O) activities.

**Remember:** Async execution does not mean that every task runs at the exact same time. It allows tasks to make progress during overlapping waiting periods.

## 3. Synchronous vs Asynchronous

| Synchronous | Asynchronous |
|---|---|
| Tasks usually execute one after another | Tasks can make progress while another task is waiting |
| Waiting can keep execution from moving to the next task | An async task can suspend while other async tasks progress |
| Independent 2-second waits, one after another, take about 6 seconds for 3 tasks | Three overlapping 2-second waits can take about 2 seconds overall |

## 4. Python's `asyncio` Module

Python provides the `asyncio` module for writing asynchronous programs.

```python
import asyncio
```

We will use `asyncio` to define asynchronous functions, wait asynchronously, run an async program, and run multiple async operations together.

## 5. The `async` Keyword

We use `async def` to define an asynchronous function.

```python
async def greet():
    print("Hello")
```

Calling an asynchronous function does not immediately execute its body like a normal function call. It creates a **coroutine object**, which needs to be awaited or run by an asynchronous execution mechanism.

## 6. What Is a Coroutine?

A **coroutine** is an object created when an asynchronous function is called. It represents asynchronous work that can be run and suspended while waiting.

```python
import asyncio

async def greet():
    print("Hello")

result = greet()
print(result)
```

The output will look similar to:

```text
<coroutine object greet at ...>
```

`Hello` is not printed because we only created the coroutine object; we did not execute it.

## 7. The `await` Keyword

The `await` keyword is used inside an asynchronous function to wait for an asynchronous operation to finish. It suspends the current coroutine at that point, allowing other async work to make progress.

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Welcome")

asyncio.run(greet())
```

**Output:**
```text
Hello
(approximately 2 seconds wait)
Welcome
```

### Understanding the code

- `async def greet()` defines an asynchronous function.
- `print("Hello")` prints immediately when the coroutine begins running.
- `await` pauses the current coroutine while the awaited operation is pending.
- `asyncio.sleep(2)` creates a 2-second asynchronous delay.
- After the delay, `print("Welcome")` runs.
- `asyncio.run(greet())` runs the async program.

## 8. `asyncio.sleep()`

`asyncio.sleep()` provides a delay without blocking the event loop in the same way that normal `time.sleep()` blocks the current thread.

### Normal sleep with `time.sleep()`

```python
import time

print("Hello")
time.sleep(2)
print("Welcome")
```

`time.sleep(2)` blocks the current thread for 2 seconds.

### Asynchronous sleep with `asyncio.sleep()`

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Welcome")

asyncio.run(greet())
```

When the coroutine reaches `await asyncio.sleep(2)`, it suspends. The event loop can use that time to progress other async tasks.

| `time.sleep()` | `asyncio.sleep()` |
|---|---|
| Blocking sleep | Asynchronous sleep |
| Blocks the current thread | Suspends the current coroutine while waiting |
| Other async work on that same event loop cannot progress during the blocking call | Other ready async tasks can progress during the wait |

## 9. `asyncio.gather()` — Running Multiple Async Operations Together

`asyncio.gather()` is used to run multiple awaitable operations concurrently and wait until all of them finish. It can also collect their returned results.

```python
import asyncio

async def greet(name):
    print("Hello", name)
    await asyncio.sleep(2)
    print("Welcome", name)

async def main():
    await asyncio.gather(
        greet("A"),
        greet("B"),
        greet("C")
    )

asyncio.run(main)
```

**Typical output:**
```text
Hello A
Hello B
Hello C
(approximately 2 seconds wait)
Welcome A
Welcome B
Welcome C
```

The exact order of printed lines can depend on scheduling, but all three coroutines can overlap their 2-second waiting periods. The total time is approximately 2 seconds rather than 6 seconds.

## 10. Understanding `asyncio.run()`

`asyncio.run()` is used to run an asynchronous program from the normal Python program entry point.

```python
asyncio.run(main())
```

- It starts the async execution of `main()`.
- It manages the event loop for this run.
- It waits for `main()` to finish before the program continues/exits.

In regular `.py` files, use `asyncio.run(main())` to start the async program. Some interactive environments, such as notebooks, support top-level `await main()`.

## 11. Program 1: Calling Two Coroutines with `asyncio.gather()`

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to Python")

async def main():
    await asyncio.gather(greet(), greet())

asyncio.run(main())
```

### Output (typical)

```text
Hello
Hello
(approximately 4 seconds wait)
Welcome to Python
Welcome to Python
```

### Dry Run

1. `asyncio.run(main())` starts `main()`.
2. `main()` reaches `asyncio.gather()` and starts both `greet()` coroutines.
3. Each coroutine prints `Hello`.
4. Each reaches `await asyncio.sleep(4)` and suspends.
5. Their 4-second waiting periods overlap.
6. After the waiting period, both continue and print `Welcome to Python`.

**Time comparison:** Sequentially waiting twice for 4 seconds would take about 8 seconds. With the two async waits overlapping, this program takes approximately 4 seconds.

## 12. Program 2: Collecting Results with `asyncio.gather()`

```python
import asyncio

async def square(n):
    await asyncio.sleep(2)
    return n * n

async def main():
    results = await asyncio.gather(
        square(2),
        square(3),
        square(4)
    )
    print(results)

asyncio.run(main())
```

**Output:**
```text
[4, 9, 16]
```

### Dry Run

| Function call | Calculation | Returned value |
|---|---|---:|
| `square(2)` | `2 * 2` | 4 |
| `square(3)` | `3 * 3` | 9 |
| `square(4)` | `4 * 4` | 16 |

All three functions wait for 2 seconds concurrently. After all are complete, `gather()` returns a list of results.

**Important:** The result list follows the order of the calls passed to `gather()`, not necessarily the order in which the tasks finish.

## 13. Important Keywords and Functions

| Keyword / Function | Purpose |
|---|---|
| `async` | Marks a function as asynchronous when used with `def` |
| `async def` | Defines an asynchronous function |
| Coroutine | Object created by calling an async function; represents async work |
| `await` | Suspends the current coroutine while waiting for an awaitable operation |
| `asyncio.sleep()` | Performs an asynchronous delay |
| `asyncio.gather()` | Runs multiple awaitable operations concurrently and waits for them; can collect results |
| `return` | Sends a result back from a function/coroutine |
| `asyncio.run()` | Runs the top-level asynchronous function in a regular Python program |

## 14. Common Mistakes

### Mistake 1: Calling an async function without running/awaiting it

```python
async def greet():
    print("Hello")

greet()  # This creates a coroutine; it does not run the body by itself.
```

### Mistake 2: Using `await` outside an async function

In a regular Python `.py` file, `await` must be used inside an asynchronous function. Some interactive environments allow top-level `await`.

### Mistake 3: Forgetting `async` before the function definition

If a function needs to use `await`, define it using `async def`.

### Mistake 4: Thinking `gather()` always returns results in completion order

The results returned by `gather()` are in the same order as the awaitables were passed to it.

## 15. Practice Questions

1. What is synchronous execution?
2. What is asynchronous execution?
3. Write any two differences between synchronous and asynchronous execution.
4. Which Python module is commonly used for Async IO?
5. What is the purpose of the `async` keyword?
6. What is a coroutine?
7. What is the purpose of `await`?
8. What is the difference between `time.sleep()` and `asyncio.sleep()`?
9. What is the purpose of `asyncio.gather()`?
10. What does `asyncio.run()` do?
11. Predict the output of the first program in Section 11.
12. What list is returned by the calls `square(2)`, `square(3)`, and `square(4)` in Section 12?
13. If three async operations each await `asyncio.sleep(3)` and are run with `asyncio.gather()`, approximately how long might their overlapping waits take?
14. Does `asyncio.gather()` return results in the order tasks finish or the order calls were provided?

## 16. Quick Revision

- **Async IO** helps a program make progress on other tasks while an operation is waiting.
- **`async def`** defines an asynchronous function.
- Calling an async function creates a coroutine object; it does not automatically execute the function body.
- **`await`** suspends the current coroutine while waiting for an asynchronous operation.
- **`asyncio.sleep()`** performs a non-blocking asynchronous delay.
- **`asyncio.gather()`** runs multiple awaitable operations concurrently, waits for all of them, and can collect their results.
- **`asyncio.run()`** runs the top-level async program in a regular Python script.
