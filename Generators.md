# Python Generators – Student Notes

## 1. What is a Generator?

A **generator** is a special type of function that produces values one at a time, whenever they are needed, instead of producing all the values at once.

Generators are useful when we want to work with a sequence of values without storing the entire sequence in memory at once.

### Example: Regular function vs generator

A regular function may return a complete list:

```python
def numbers():
    return [1, 2, 3, 4, 5]

print(numbers())
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

A generator produces values one by one as they are requested.

---

## 2. The `yield` Keyword

Generators are commonly created using `yield` instead of `return`.

- `return` sends a value back and ends the function.
- `yield` sends a value back, pauses the function, and remembers where it stopped. The function can continue from that point when asked for another value.

### Program 1: A simple generator

```python
def number_generator():
    yield 1
    yield 2
    yield 3

for number in number_generator():
    print(number)
```

**Output:**

```text
1
2
3
```

### How it works

1. Calling `number_generator()` creates a generator object.
2. The `for` loop requests the first value. The function runs until it reaches `yield 1` and gives back `1`.
3. The next request continues from where it paused and gives back `2`.
4. The next request gives back `3`.
5. When there are no more values, the generator finishes.

The generator does not run all its statements immediately when it is called. It starts running as values are requested.

---

## 3. Generator Object

Calling a generator function does not immediately execute its body. It creates a generator object.

### Program 2: Printing a generator object

```python
def simple_generator():
    yield "Hello"
    yield "Python"

result = simple_generator()
print(result)
```

**Output (format may vary):**

```text
<generator object simple_generator at ...>
```

The output represents a generator object, not the yielded values. To get the values, iterate over the generator or request them using `next()`.

---

## 4. Using `next()` with a Generator

The `next()` function requests the next value from a generator.

### Program 3: Calling `next()`

```python
def count_generator():
    yield 10
    yield 20
    yield 30

g = count_generator()

print(next(g))
print(next(g))
print(next(g))
```

**Output:**

```text
10
20
30
```

### Dry run

| Call | Value produced |
|---|---:|
| `next(g)` – first call | 10 |
| `next(g)` – second call | 20 |
| `next(g)` – third call | 30 |

Each `next()` resumes the generator from its previous pause and asks it to produce the next value.

If `next()` is called after all values have been produced, the generator ends and Python raises `StopIteration`.

---

## 5. Generator with a Loop

Generators can use loops to produce a sequence of values.

### Program 4: Generate numbers from 1 to 5

```python
def count_up_to_five():
    for i in range(1, 6):
        yield i

for value in count_up_to_five():
    print(value)
```

**Output:**

```text
1
2
3
4
5
```

### Explanation

- The loop generates numbers from 1 through 5.
- `yield i` provides the current value to the caller.
- The generator pauses after each yielded value and continues when another value is requested.

---

## 6. Generator vs Normal Function (`return` and `yield`)

### Program 5: Comparing `return` and `yield`

```python
def normal_function():
    return 1
    return 2
    return 3


def generator_function():
    yield 1
    yield 2
    yield 3

print(normal_function())

for value in generator_function():
    print(value)
```

**Output:**

```text
1
1
2
3
```

### Why?

In `normal_function()`, the first `return 1` ends the function. The later return statements are never reached.

In `generator_function()`, each `yield` gives a value and pauses. The generator can resume to produce the next value.

| `return` | `yield` |
|---|---|
| Ends the function | Pauses the generator function |
| Normally returns a value | Produces a value, then can continue later |
| Further statements in the function do not execute after return | Execution can resume after yield when another value is requested |

---

## 7. Practical Example: Generate Even Numbers

### Program 6

```python
def even_numbers(limit):
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number

for even in even_numbers(10):
    print(even)
```

**Output:**

```text
2
4
6
8
10
```

### Explanation

- `limit` tells us the maximum number to check.
- The loop checks each number from 1 up to the limit.
- `% 2 == 0` checks if a number is divisible by 2.
- When the number is even, `yield` provides it to the caller.

---

## 8. Practical Example: Squares Using a Generator

### Program 7

```python
def squares(limit):
    for number in range(1, limit + 1):
        yield number * number

for value in squares(5):
    print(value)
```

**Output:**

```text
1
4
9
16
25
```

This generator calculates and produces one square at a time as the loop requests each value.

---

## 9. Why are Generators Useful?

Suppose we need to work with a very large sequence of numbers.

A list stores all generated values together in memory. A generator can produce each value only when needed, so it often uses less memory for large sequences.

### Program 8: List vs Generator

```python
# List: stores all values
numbers_list = [number for number in range(1, 6)]

# Generator expression: produces values as requested
numbers_generator = (number for number in range(1, 6))

print(numbers_list)
print(numbers_generator)
```

**Output (generator object's address/representation may vary):**

```text
[1, 2, 3, 4, 5]
<generator object <genexpr> at ...>
```

The list prints all its values. The generator expression prints a generator object because it has not been iterated over yet.

To print its values:

```python
for number in numbers_generator:
    print(number)
```

**Output:**

```text
1
2
3
4
5
```

---

## 10. Generator Expressions

A generator expression is a compact way of creating a generator. It looks similar to a list comprehension, but uses parentheses `()` instead of square brackets `[]`.

### Program 9: Generator expression

```python
squares = (number * number for number in range(1, 6))

for value in squares:
    print(value)
```

**Output:**

```text
1
4
9
16
25
```

### Difference in syntax

```python
# List comprehension – creates a list
squares_list = [number * number for number in range(1, 6)]

# Generator expression – creates a generator
squares_generator = (number * number for number in range(1, 6))
```

| List comprehension | Generator expression |
|---|---|
| Uses `[]` | Uses `()` |
| Creates/stores a list of values | Produces values as requested |
| May use more memory for a large sequence | Often more memory-efficient for large sequences |

---

## 11. A Generator Can Be Used Only Once Through Its Values

Once a generator has produced all of its values, it is exhausted. Iterating over it again will not produce those values unless a new generator is created.

### Program 10

```python
def letters():
    yield "A"
    yield "B"
    yield "C"

g = letters()

for letter in g:
    print(letter)

print("Again:")
for letter in g:
    print(letter)
```

**Output:**

```text
A
B
C
Again:
```

The second loop prints nothing because the generator has already produced all its values.

---

## 12. Common Mistakes

### Mistake 1: Expecting a generator call to print or return all values

```python
def my_generator():
    yield 1
    yield 2

print(my_generator())
```

This prints the generator object's representation, not `1` and `2`. Use a loop or `next()` to retrieve its values.

### Mistake 2: Using `return` instead of `yield` when multiple values are intended

```python
def numbers():
    return 1
    return 2
```

Only `1` is returned; the function ends immediately. Use `yield` when the function should produce a sequence of values over multiple requests.

### Mistake 3: Calling `next()` too many times

After the generator is exhausted, another `next()` raises `StopIteration`. Normally, use a `for` loop to iterate safely over all available values.

### Mistake 4: Expecting the same generator to restart

A generator that has already been exhausted does not automatically restart. Call the generator function again to create a new generator object.

---

## 13. Quick Revision

| Term | Meaning |
|---|---|
| Generator | Produces values one at a time as requested |
| `yield` | Produces a value and pauses generator execution |
| `next()` | Requests the next value from a generator |
| Generator object | Object created when a generator function is called |
| `StopIteration` | Indicates that a generator has no more values to provide |
| Generator expression | Compact generator creation syntax using parentheses |
| `return` | Ends a function and returns a value |
| Memory efficiency | Generators can avoid storing an entire large sequence at once |

---

# Practice Programs

Try solving these questions on your own. Use `yield` wherever the question asks you to create a generator.

## Level 1 – Basics

1. Write a generator function that yields the numbers from 1 to 10. Print the values using a `for` loop.
2. Write a generator that yields the first 10 natural numbers.
3. Create a generator that yields the numbers 10, 20, 30, 40, and 50 using separate `yield` statements. Retrieve the values using `next()`.
4. Write a generator function that yields the letters of the word `PYTHON` one at a time.
5. Write a generator that takes a number `n` and yields numbers from `n` down to 1.

## Level 2 – Logic Building

6. Write a generator that yields all even numbers from 1 to a user-provided limit.
7. Write a generator that yields all odd numbers from 1 to a user-provided limit.
8. Write a generator that takes a number `n` and yields the square of every number from 1 to `n`.
9. Write a generator that takes a number `n` and yields the cube of every number from 1 to `n`.
10. Write a generator that yields the multiplication table of a given number from 1 to 10.

## Level 3 – Application

11. Write a generator that takes a list of numbers and yields only the positive numbers.
12. Write a generator that takes a list of numbers and yields only numbers divisible by 5.
13. Write a generator that takes a string and yields each vowel found in it.
14. Write a generator that takes a list of numbers and yields the running total. For example, for `[2, 4, 6, 8]`, it should yield `2`, `6`, `12`, and `20`.
15. Write a generator that produces Fibonacci numbers up to a specified count.

---

## Important Instructions

- Write the programs yourself and understand each line.
- Do not just memorize the output; trace how each value is yielded.
- For every program, add comments explaining the logic used.
- Test your code with different inputs.
- Practice using both `for` loops and `next()` where applicable.
