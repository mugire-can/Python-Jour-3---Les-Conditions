# Python Day 3 Exercises - Detailed Documentation

## Overview

This document provides detailed information about each of the 8 programming exercises focusing on conditional statements and control flow in Python.

---

## Job 1: Compare Two Values

**Objective**: Determine if two input values are equal.

**Key Concepts**:
- Input handling with `input()`
- String comparison with `==`
- if-else conditional statements

**Example**:
```
Input: "hello" and "hello"
Output: ✓ Valeur1 est égal à valeur2
```

**Learning Points**:
- String comparison is case-sensitive
- `==` checks for equality
- The `else` clause provides alternative action

---

## Job 2: Voting Eligibility

**Objective**: Determine if someone can vote based on age.

**Key Concepts**:
- Type conversion with `int()`
- Comparison operators (`>=`, `<`)
- Input validation with try-except

**Example**:
```
Input: 25
Output: ✓ À 25 ans, tu peux voter
```

**Learning Points**:
- Age must be >= 18 to vote (in France)
- Type conversion can raise `ValueError`
- Error handling improves user experience

---

## Job 3: Skip Specific Numbers

**Objective**: Print numbers 0-100, skipping specific values (26, 37, 88).

**Key Concepts**:
- `for` loop with `range()`
- `continue` statement for loop control
- Membership testing with `in`

**Example**:
```
Output: 0 1 2 3 ... 25 27 28 ... 36 38 39 ... 87 89 90 ... 100
```

**Learning Points**:
- `continue` skips current iteration
- The `in` operator checks list membership
- Loop formatting improves readability

---

## Job 4: FizzBuzz Problem

**Objective**: Classic FizzBuzz: Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both.

**Key Concepts**:
- Modulo operator `%` for remainder calculation
- Multiple conditions with `and`
- elif chains for multiple conditions

**Example**:
```
Output: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...
```

**Learning Points**:
- `x % 3 == 0` means x is divisible by 3
- Condition order matters (check FizzBuzz before Fizz/Buzz)
- This is a classic interview question

---

## Job 5: Find Prime Numbers

**Objective**: Find all prime numbers between 2 and 1000.

**Key Concepts**:
- Function definition and reusability
- Primality testing algorithm
- List comprehensions (in implementation)
- Algorithm efficiency (checking up to √n)

**Example**:
```
Output: 2 3 5 7 11 13 17 19 23 29 ... 997
Found: 168 primes
```

**Prime Testing Algorithm**:
- A prime number is only divisible by 1 and itself
- Only need to check divisors up to √n
- Returns False immediately upon finding a divisor

**Learning Points**:
- Functions encapsulate reusable logic
- Algorithm optimization matters
- There are 168 primes between 2-1000

---

## Job 6: Even/Odd Checker

**Objective**: Determine if a number is even or odd.

**Key Concepts**:
- Modulo operator `%` for divisibility
- f-strings for string interpolation
- Type conversion validation

**Example**:
```
Input: 42
Output: ✓ Le nombre 42 est pair
```

**Learning Points**:
- `n % 2 == 0` → even
- `n % 2 != 0` → odd
- f-strings are modern Python string formatting

---

## Job 7: String Pyramid

**Objective**: Build a pyramid pattern from user input string.

**Key Concepts**:
- String slicing with `[start:end]`
- Index management in loops
- Break condition handling

**Example**:
```
Input: "abcdefghij"
Output:
a
ab
abc
abcd
abcde
```

**Algorithm**:
1. Start at index 0
2. Each line i contains i characters from string[index:index+i]
3. Increment index after each line
4. Stop when not enough characters remain

**Learning Points**:
- String slicing doesn't modify original
- Index tracking is important for iteration
- Loop termination conditions matter

---

## Job 8: Triangle Validator and Classifier

**Objective**: Validate if three sides form a valid triangle and classify its type.

**Key Concepts**:
- Triangle inequality theorem validation
- Pythagorean theorem for right triangles
- Function composition

**Triangle Types**:
- **Équilatéral**: All three sides equal (a=b=c)
- **Isocèle**: Exactly two sides equal (a=b or b=c or a=c)
- **Rectangle**: Right angle (a²+b²=c²)
- **Rectangle Isocèle**: Right angle AND two equal sides
- **Scalène**: All sides different (no special properties)

**Validation (Triangle Inequality)**:
```
a + b > c
a + c > b
b + c > a
```
All three must be true.

**Pythagorean Theorem for Right Triangles**:
```
a² + b² = c²  (where c is longest side)
```

**Example**:
```
Input: 3, 4, 5
Output: ✓ Triangle valide: rectangle
```

**Learning Points**:
- Geometry validation improves code complexity
- Multiple function calls in sequence (composition)
- Float comparison can have precision issues

---

## Running the Exercises

### Interactive Menu
```bash
python main.py
```
Select individual exercises or run all at once.

### Run Tests
```bash
pytest tests_exercises.py -v
```

### Direct Import
```python
from jobs import job_1_compare_values, job_5_prime_numbers
job_5_prime_numbers()
```

---

## Tips and Tricks

1. **Input Validation**: Always validate user input before using it
2. **Function Reusability**: Extract functions to reuse logic (see `est_premier`)
3. **Loop Control**: Use `continue` and `break` to control flow efficiently
4. **Algorithm Efficiency**: Optimize where possible (e.g., checking to √n for primes)
5. **Type Hints**: Add annotations for code clarity
6. **Error Handling**: Use try-except for user input

---

## Common Mistakes to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| `else if` instead of `elif` | SyntaxError | Use Python's `elif` |
| `=` instead of `==` in condition | Assignment instead of comparison | Use `==` for comparison |
| Forgetting `continue` | Loop processes unwanted items | Use `continue` to skip |
| Checking to n instead of √n | Inefficient prime checking | Check to `int(num**0.5)` |
| Not handling input errors | Crashes on invalid input | Use try-except |

---

## Further Learning

- [Python Docs - if statements](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Docs - for loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Docs - Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Triangle Inequality Theorem](https://en.wikipedia.org/wiki/Triangle_inequality)
- [Pythagorean Theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)
