# Python Day 3 - Conditions (Jour 3 - Les Conditions) 🐍

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)

A comprehensive collection of Python exercises focusing on conditional statements and control flow from **La Plateforme** Python course. Refactored with modular architecture, unit tests, and extensive documentation.

## 📋 Project Overview

This project contains **8 progressive programming exercises** demonstrating fundamental Python concepts with production-quality code:

| # | Exercise | Concepts | Status |
|---|----------|----------|--------|
| 1 | **Compare Values** | String comparison, if-else | ✅ |
| 2 | **Voting Eligibility** | Type conversion, age validation | ✅ |
| 3 | **Skip Numbers** | for-loop, continue statement | ✅ |
| 4 | **FizzBuzz** | Modulo operator, elif chains | ✅ |
| 5 | **Prime Numbers** | Functions, algorithms, list comprehension | ✅ |
| 6 | **Even/Odd Checker** | Modulo operator, f-strings | ✅ |
| 7 | **String Pyramid** | String slicing, index management | ✅ |
| 8 | **Triangle Validator** | Geometry, function composition | ✅ |

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/mugire-can/Python-Jour-3---Les-Conditions.git
cd Python-Jour-3---Les-Conditions

# Install dependencies (optional, only for testing)
pip install -r requirements.txt
```

### Run Interactive Menu

```bash
python main.py
```

**Menu Features**:
- Run individual exercises
- Execute all exercises in sequence
- View exercise descriptions
- Performance timing for each exercise

### Run All Original Exercises

```bash
python "Projet Jour 3.py"
```

### Run Unit Tests

```bash
# Run all tests with verbose output
pytest tests_exercises.py -v

# Run with coverage report
pytest tests_exercises.py --cov=jobs
```

## 📁 Project Structure

```
Python-Jour-3---Les-Conditions/
├── main.py                    # Interactive menu system (NEW)
├── jobs.py                    # Modular exercise functions (NEW)
├── config.py                  # Configuration settings (NEW)
├── tests_exercises.py         # Unit tests (NEW)
├── Projet Jour 3.py          # Original all-in-one script
├── requirements.txt           # Python dependencies (NEW)
├── README.md                  # This file
├── .gitignore                 # Git exclusions
├── EXERCISES.md              # Detailed exercise documentation (NEW)
└── EXAMPLES.md               # Example inputs and outputs (NEW)
```

## 🎯 Key Features

### ✨ Modern Python Practices
- **Type Hints**: Full type annotations for all functions
- **Docstrings**: Comprehensive documentation for all functions
- **Error Handling**: Input validation with try-except blocks
- **f-Strings**: Modern string formatting throughout

### 🧪 Quality Assurance
- **Unit Tests**: 20+ test cases covering all major functions
- **Test Coverage**: Prime number validation, triangle classification
- **Integration Tests**: Multi-function workflow validation

### 📚 Documentation
- **Detailed Guide**: Complete exercise explanations in `EXERCISES.md`
- **Examples**: Input/output examples for all exercises in `EXAMPLES.md`
- **Configuration**: Customizable settings in `config.py`

### 🎮 User Experience
- **Interactive Menu**: User-friendly exercise selection
- **Performance Timing**: Track execution time for each exercise
- **Visual Feedback**: Emoji indicators (✓, ✗, ⚠, 🎯) for clarity
- **Error Recovery**: Graceful handling of invalid inputs

## 📖 Topics Covered

### Control Flow
- Conditional statements (`if`, `elif`, `else`)
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators (`and`, `or`)

### Loops & Flow Control
- `for` loops with `range()`
- Loop control with `continue` and `break`
- Index management and loop termination

### Functions
- Function definition and return statements
- Function composition and reusability
- Parameter passing and type hints

### Algorithms
- Prime number detection (optimized to √n)
- Triangle inequality validation
- Pythagorean theorem implementation

### Data Structures & Strings
- String comparison and slicing
- List comprehensions
- Index manipulation

## 💡 Code Examples

### Using Individual Functions

```python
from jobs import est_premier, est_constructible, type_de_triangle

# Check if number is prime
if est_premier(17):
    print("17 is prime!")

# Validate triangle
if est_constructible(3, 4, 5):
    triangle_type = type_de_triangle(3, 4, 5)
    print(f"Valid triangle: {triangle_type}")  # Output: Valid triangle: rectangle
```

### Running from Module

```python
from jobs import job_5_prime_numbers

# Find all primes between 2-1000
job_5_prime_numbers()
```

## 🧪 Testing

### Test Categories

**Prime Number Tests**:
- Small primes (2, 3, 5, 7)
- Composite numbers (4, 6, 8, 9)
- Large primes (97, 101, 997)
- Negative numbers and edge cases

**Triangle Validation Tests**:
- Valid triangles (equilateral, isosceles, scalene)
- Right triangles (Pythagorean theorem)
- Invalid triangles (violate triangle inequality)
- Edge cases (degenerate triangles)

### Run Tests

```bash
# All tests
pytest tests_exercises.py -v

# Specific test class
pytest tests_exercises.py::TestPrimeNumbers -v

# With coverage
pytest tests_exercises.py --cov=jobs --cov-report=html
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
VOTING_AGE = 18              # Change voting age
PRIME_RANGE_END = 1000       # Adjust prime number range
MAX_PYRAMID_LINES = 20       # Pyramid size limit
SHOW_TIMING = True           # Enable/disable performance timing
VERBOSE = True               # Enable/disable detailed output
```

## 🎓 Learning Outcomes

After completing these exercises, you'll understand:

✅ How to use conditional statements effectively  
✅ Loop control with `continue` and `break`  
✅ Function definition and reusability  
✅ Input validation and error handling  
✅ Basic algorithm design (prime checking, geometry)  
✅ String manipulation and slicing  
✅ Professional Python practices (type hints, docstrings)  
✅ Unit testing and test-driven development  

## 📚 Documentation Files

- **[EXERCISES.md](EXERCISES.md)** - Detailed breakdown of each exercise with learning points
- **[EXAMPLES.md](EXAMPLES.md)** - Example inputs and outputs for all exercises
- **[Projet Jour 3.py](Projet%20Jour%203.py)** - Original all-in-one implementation

## 🔧 Requirements

- **Python 3.7+** (3.8+ recommended for type hints)
- **pytest 7.0+** (for testing, optional)

```bash
pip install -r requirements.txt
```

## 🚢 Project Statistics

- **Total Functions**: 12 (8 exercises + 4 utility functions)
- **Lines of Code**: 350+ (well-documented)
- **Test Cases**: 20+
- **Documentation**: 2000+ lines across 3 files

## 👨‍💻 Usage Tips

### For Learning
1. Start with `main.py` to explore exercises interactively
2. Read `EXERCISES.md` for detailed explanations
3. Study `jobs.py` to see professional Python practices
4. Review `tests_exercises.py` to understand testing

### For Production Use
1. Import functions from `jobs.py` directly
2. Add your own functionality
3. Run tests to ensure reliability
4. Reference `config.py` for customization

## 🎯 Common Use Cases

```python
# Check if year is leap year (extend Job 6)
def is_leap_year(year: int) -> bool:
    from jobs import est_premier
    # Can reuse functions!

# Validate user input (extend Job 2)
def get_valid_age() -> int:
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 150:
                return age
        except ValueError:
            print("Invalid input")
```

## 📝 Notes

- All exercises include input validation
- Performance optimized (e.g., prime checking to √n)
- Code follows PEP 8 style guidelines
- Comprehensive error handling throughout

## 🔗 Resources

- [Python Official Docs - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Type Hints in Python](https://docs.python.org/3/library/typing.html)
- [Triangle Inequality Theorem](https://en.wikipedia.org/wiki/Triangle_inequality)

## 👤 Author

**La Plateforme** - Python Course  
Refactored and enhanced with modern practices

## 📄 License

MIT License - See LICENSE file for details

---

## ✨ What's New (v2.0)

- 🔄 Refactored into modular functions
- 📋 Interactive menu system
- 🧪 Comprehensive unit tests (20+ cases)
- 📚 Detailed documentation (3 files)
- 💾 Configuration management
- ✅ Input validation on all exercises
- ⏱️ Performance timing
- 🎨 User-friendly emoji indicators

**Last Updated**: 2025-12-28  
**Status**: Production Ready ✅
