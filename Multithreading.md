# Python Multithreading — Student Notes

## 1. What is a Process?

A **process** is a program that is currently running.

Examples:
- Opening Chrome creates a running process.
- Opening VS Code creates a running process.
- Running a Python program creates a Python process.

A process has its own resources, such as memory and execution state, managed by the operating system.

## 2. What is a Thread?

A **thread** is an execution path within a process. A process can have one or more threads.

Think of a restaurant:
- Restaurant = process
- Workers = threads
- Orders = tasks

If one worker has to complete every order before starting the next, work can take longer. Multiple workers can work on separate orders, especially when one is waiting.

## 3. Process vs Thread

| Process | Thread |
|---|---|
| A running program | An execution path inside a process |
| Has its own memory space | Threads within a process share memory |
| Generally heavier to create | Generally lighter to create |
| Processes are isolated from one another | Threads can access shared data in the same process |

## 4. Sequential vs Concurrent Execution

### Sequential execution

Tasks execute one after another. The next task starts after the previous one finishes.

```python
import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 completed")

task1()
task2()
```

**Expected behavior:** Task 1 finishes before Task 2 begins. Total time is about 4 seconds.

### Concurrent execution

Concurrency means multiple tasks can make progress during overlapping time periods. Threads can overlap their waiting time, which is useful when tasks are independent.

## 5. Why do we need multithreading?

Imagine a program needs to:
1. Download a file
2. Send an email
3. Fetch information from a server

If each task waits for an external response, doing them one after another wastes time. Threads can allow tasks to overlap while one task is waiting.

**Multithreading** means using multiple threads within one process to perform different tasks concurrently.

It is often useful for **I/O-bound tasks**, such as downloading files, waiting for network responses, or reading files. It does not automatically make every program faster. CPU-heavy work may not speed up with threads in standard CPython.

## 6. Python `threading` Module

Python provides the built-in `threading` module to create and manage threads.

```python
import threading
```

The main class we'll use is `threading.Thread()`.

## 7. Creating a Thread: `Thread()` and `target`

`Thread()` creates a thread object. The `target` parameter tells the thread which function to execute.

```python
import threading

def greet():
    print("Hello from the thread")

t1 = threading.Thread(target=greet)
```

- `threading.Thread()` creates a thread object.
- `target=greet` passes the function to the thread to execute.
- Notice we write `greet`, not `greet()`. Parentheses would call the function immediately instead of passing the function itself as the target.

Creating the thread object does not start it. To start it, call `start()`.

## 8. `start()` — Start a Thread

The `start()` method starts the thread. Python schedules the target function to run in that thread.

```python
import threading

def greet():
    print("Hello from the thread")

t1 = threading.Thread(target=greet)
t1.start()
print("Main program continues")
```

The two print statements may appear in either order because the main thread and the new thread can make progress independently. The exact order is not guaranteed.

**Important:** Call `start()` to launch a thread. Calling `t1.run()` directly does not start a separate thread; it runs the target in the current thread.

## 9. `sleep()` — Pause Execution

`time.sleep(seconds)` pauses the thread that calls it for approximately the specified duration. It is useful for simulating waiting in examples.

```python
import time

print("Start")
time.sleep(2)
print("After waiting")
```

Output:
```text
Start
After waiting
```

There is an approximately two-second pause between the two messages.

## 10. Running Two Threads

Compare the sequential version with this multithreaded version:

```python
import threading
import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 completed")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
```

Both tasks are started without waiting for the other to finish. Their waiting periods can overlap, so this example typically takes about 2 seconds instead of 4 seconds.

**The output order is not guaranteed.** For example, the “started” messages and “completed” messages may appear in a different order on different runs.

## 11. `join()` — Wait for a Thread to Finish

When a thread is started, the main thread can continue running. If we need the main thread to wait for a worker thread to finish, use `join()`.

```python
import threading
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task completed")

t1 = threading.Thread(target=task)
t1.start()
t1.join()
print("Main program ended")
```

Output:
```text
Task started
Task completed
Main program ended
```

`t1.join()` makes the thread that calls it (here, the main thread) wait until `t1` has completed.

### Using `join()` with two threads

```python
import threading
import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(3)
    print("Task 2 completed")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
print("Both tasks finished")
```

The main thread waits until both threads complete before printing `Both tasks finished`. The two tasks' sleep periods overlap, so total time is approximately 3 seconds, not 5 seconds.

## 12. Passing Arguments using `args`

If the target function needs arguments, pass them through the `args` parameter. `args` must be a tuple.

```python
import threading

def greet(name):
    print("Hello", name)

t1 = threading.Thread(target=greet, args=("Aarav",))
t1.start()
t1.join()
```

Output:
```text
Hello Aarav
```

**Remember:** A one-item tuple needs a trailing comma: `("Aarav",)`.

### Passing more than one argument

```python
import threading

def add(a, b):
    print("Sum:", a + b)

t1 = threading.Thread(target=add, args=(10, 20))
t1.start()
t1.join()
```

Output:
```text
Sum: 30
```

## 13. Synchronizing Threads

**Thread synchronization** means coordinating threads so they access shared resources safely and in the required order.

### Why is synchronization necessary?

Threads within the same process can share data. If two threads update the same variable at the same time, their operations can interfere, and the result may not be what we expected. This problem is called a **race condition**.

### Example: Shared counter without a lock

```python
import threading

counter = 0

def increase_counter():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=increase_counter)
t2 = threading.Thread(target=increase_counter)

t1.start()
t2.start()
t1.join()
t2.join()

print("Counter:", counter)
```

Both threads update the same shared variable. In general, unsynchronized shared-data updates can cause race conditions. Depending on the operation, Python version, and execution circumstances, this example may or may not visibly produce a wrong value; it is not a reliable demonstration of a race every time.

### `Lock()` — Protect Shared Data

A lock allows only one thread at a time to enter a protected section of code. A thread must acquire the lock before entering and release it afterward.

```python
import threading

counter = 0
lock = threading.Lock()

def increase_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increase_counter)
t2 = threading.Thread(target=increase_counter)

t1.start()
t2.start()
t1.join()
t2.join()

print("Counter:", counter)
```

Expected output:
```text
Counter: 200000
```

`with lock:` automatically acquires the lock before the indented code runs and releases it when that block exits—even if an exception occurs. This is safer than manually acquiring and releasing the lock.

### How a lock works

1. Thread 1 enters the protected section and acquires the lock.
2. Thread 2 tries to enter but must wait while the lock is held.
3. Thread 1 finishes the protected code and releases the lock.
4. Thread 2 can then acquire the lock and enter.

Use locks for short sections that modify or access shared data in ways that must not overlap. Do not lock large portions of code unnecessarily because waiting reduces concurrency.

## 14. `acquire()` and `release()` (Manual Locking)

A lock can also be managed manually:

```python
import threading

lock = threading.Lock()

def task():
    lock.acquire()
    try:
        print("Inside locked section")
    finally:
        lock.release()
```

- `lock.acquire()` obtains the lock. If another thread holds it, this thread waits.
- `lock.release()` releases it so another thread can acquire it.
- The `try/finally` ensures the lock is released even if an exception happens inside the protected section.

For most beginner code, prefer `with lock:` because it handles releasing the lock automatically.

## 15. Concurrency vs. Parallelism

- **Concurrency:** Multiple tasks make progress over overlapping periods. They may take turns or run in parallel.
- **Parallelism:** Multiple tasks are literally executing at the same time, such as on separate CPU cores.

Multithreading does not guarantee that tasks will execute simultaneously on different cores.

## 16. I/O-Bound vs. CPU-Bound (Basic)

### I/O-bound tasks

Tasks that spend much of their time waiting for input/output, such as:
- Downloading files
- Sending network requests
- Reading files
- Waiting for a database response

Threads are often useful for these tasks because another task can progress while one is waiting.

### CPU-bound tasks

Tasks that spend most of their time doing calculations, such as:
- Calculating many prime numbers
- Large mathematical calculations
- Processing large amounts of data

In standard CPython, multithreading may not speed up CPU-heavy Python code because of the Global Interpreter Lock (GIL). For this level, remember: **multithreading is often helpful for I/O-bound work, but it does not automatically make every program faster.**

## 17. Quick Reference

| Method / Term | Meaning |
|---|---|
| `threading.Thread()` | Creates a thread object |
| `target` | Function the thread will execute |
| `start()` | Starts the thread |
| `sleep(seconds)` | Pauses the calling thread for the specified time |
| `join()` | Waits for a thread to finish |
| `args` | Supplies arguments to the target function (as a tuple) |
| `threading.Lock()` | Creates a lock to coordinate access to shared data |
| `acquire()` | Acquires a lock; waits if it is already held |
| `release()` | Releases a lock |
| `with lock:` | Acquires the lock for the block and releases it automatically on exit |

## 18. Important Things to Remember

- A process is a running program; a thread is an execution path inside a process.
- Sequential tasks execute one after another.
- Threads can let independent tasks overlap their waiting time.
- `Thread(target=function)` creates a thread object; it does not start it.
- `target` receives a function name without parentheses.
- `start()` starts a thread.
- `sleep()` pauses the thread that calls it.
- `join()` makes the caller wait for the specified thread to finish.
- Thread output order is not guaranteed unless coordination is used.
- Use `args` to pass function arguments; a single argument tuple needs a comma.
- Synchronization coordinates thread access to shared data.
- A lock protects a critical section from simultaneous entry by threads using that same lock.
- `with lock:` is the recommended beginner-friendly way to use a lock.
- Multithreading is often useful for I/O-bound tasks; it does not guarantee a speedup for CPU-bound work.

## 19. Practice Problems

### A. Output Prediction

**1. Predict the output:**
```python
import threading

def show():
    print("Worker")

t = threading.Thread(target=show)
t.start()
print("Main")
```
Explain why the order may vary.

**2. Predict the output:**
```python
import threading

def show():
    print("A")

t = threading.Thread(target=show)
t.start()
t.join()
print("B")
```
Can `B` print before `A`? Explain.

**3. Predict the approximate total waiting time:**
```python
import threading
import time

def task1():
    time.sleep(2)

def task2():
    time.sleep(4)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
```
Assuming the tasks are independent and mostly waiting, approximately how long will the program wait for both to finish?

### B. Write Programs

**4. Sequential execution:** Write two functions, each printing a start message, sleeping for 2 seconds, and printing a completion message. Call them sequentially and measure the total time.

**5. Two threads:** Modify Question 4 to run the functions using two threads. Start both threads and use `join()` to wait for both. Measure and compare the time.

**6. Thread arguments:** Write a function `display_student(name, roll_number)` that prints a student's name and roll number. Run it in a thread by passing arguments using `args`.

**7. Three threads:** Create three functions named `download_file`, `send_email`, and `generate_report`. Simulate each task using `sleep()` with different durations. Run all three using threads and wait for all of them using `join()`.

**8. Shared counter with lock:** Create a shared counter starting at zero. Use two threads to increase it 50,000 times each. Protect the increment using `threading.Lock()` and print the final count.

### C. Short Answer

**9.** Explain the difference between `start()` and `join()`.

**10.** What is thread synchronization? Why might a lock be needed when two threads modify shared data?

**11.** Explain the difference between concurrency and parallelism in your own words.

**12.** Give two examples of I/O-bound tasks and two examples of CPU-bound tasks. Why is multithreading often useful for I/O-bound tasks?

---

**Syllabus focus:** Process and thread, multithreading, synchronizing threads, `sleep()`, and `join()`. Make sure you understand the examples, can explain each method, and can predict output where thread scheduling makes the order variable.
