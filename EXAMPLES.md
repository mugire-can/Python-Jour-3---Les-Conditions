# Example Outputs and Expected Results

## Job 1: Compare Values

### Example 1: Equal values
```
Input: "hello" and "hello"
Output: ✓ Valeur1 est égal à valeur2
```

### Example 2: Different values
```
Input: "hello" and "world"
Output: ✗ Les deux valeurs ne sont pas égales
```

---

## Job 2: Voting Eligibility

### Example 1: Can vote
```
Input: 25
Output: ✓ À 25 ans, tu peux voter
```

### Example 2: Cannot vote
```
Input: 15
Output: ✗ À 15 ans, tu ne peux pas voter. Reviens dans 3 ans
```

### Example 3: Edge case (exactly 18)
```
Input: 18
Output: ✓ À 18 ans, tu peux voter
```

---

## Job 3: Skip Numbers

### Output (abbreviated)
```
0 1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 27 28 29 30
...
36 38 39 40 41 42 43 44 45 46
...
87 89 90 91 92 93 94 95 96 97
98 99 100
```

Numbers 26, 37, and 88 are skipped.

---

## Job 4: FizzBuzz

### Output (first 30 numbers)
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz
11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz
```

---

## Job 5: Prime Numbers

### Output (abbreviated)
```
Prime numbers between 2 and 1000:
Found 168 primes:
2 3 5 7 11 13 17 19 23 29
31 37 41 43 47 53 59 61 67 71
...
967 971 977 983 991 997
```

---

## Job 6: Even/Odd Checker

### Example 1: Even number
```
Input: 42
Output: ✓ Le nombre 42 est pair
```

### Example 2: Odd number
```
Input: 17
Output: ✓ Le nombre 17 est impair
```

---

## Job 7: String Pyramid

### Example 1
```
Input: "abcdefghij"
Output:
a
ab
abc
abcd
abcde
```

### Example 2
```
Input: "python"
Output:
p
py
pyt
pyth
pytho
```

---

## Job 8: Triangle Validator

### Example 1: Right triangle
```
Input: 3, 4, 5
Output: ✓ Triangle valide: rectangle
```

### Example 2: Equilateral triangle
```
Input: 5, 5, 5
Output: ✓ Triangle valide: équilatéral
```

### Example 3: Isosceles triangle
```
Input: 5, 5, 6
Output: ✓ Triangle valide: isocèle
```

### Example 4: Invalid triangle
```
Input: 1, 2, 5
Output: ✗ Triangle non constructible (inégalité triangulaire violée)
```

---

## Test Coverage

All functions are covered by unit tests in `tests_exercises.py`:

```
test_est_premier: 5 tests
test_est_constructible: 6 tests
test_type_de_triangle: 7 tests
test_integration: 2 tests
Total: 20+ test cases
```

Run tests with:
```bash
pytest tests_exercises.py -v
```
