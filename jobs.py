"""Modular implementation of Python Day 3 exercises.

This module contains individual functions for each programming exercise,
demonstrating conditional statements and control flow concepts.
"""

from typing import List, Tuple
from config import (
    VOTING_AGE,
    PRIME_RANGE_START,
    PRIME_RANGE_END,
    SKIP_NUMBERS,
    MAX_PYRAMID_LINES,
)


def job_1_compare_values() -> None:
    """Job 1: Compare two input values for equality.
    
    Demonstrates: Simple if-else conditional statements and string comparison.
    """
    valeur1 = input("Veuillez entrer la première valeur: ")
    valeur2 = input("Veuillez entrer la deuxième valeur: ")

    if valeur1 == valeur2:
        print("✓ Valeur1 est égal à valeur2")
    else:
        print("✗ Les deux valeurs ne sont pas égales")


def job_2_voting_eligibility() -> None:
    """Job 2: Determine voting eligibility based on age.
    
    Demonstrates: Integer input validation and age-based conditions.
    """
    try:
        age = int(input(f"Veuillez entrer votre âge: "))
        
        if age < 0:
            print("⚠ L'âge ne peut pas être négatif")
            return
            
        if age >= VOTING_AGE:
            print(f"✓ À {age} ans, tu peux voter")
        else:
            years_left = VOTING_AGE - age
            print(f"✗ À {age} ans, tu ne peux pas voter. Reviens dans {years_left} ans")
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")


def job_3_skip_numbers() -> None:
    """Job 3: Print numbers 0-100, skipping specific numbers.
    
    Demonstrates: Loop control with continue statement.
    """
    print("Numbers 0-100 (skipping 26, 37, 88):")
    count = 0
    for x in range(101):
        if x in SKIP_NUMBERS:
            continue
        print(x, end=" ")
        count += 1
        if count % 10 == 0:
            print()  # Newline every 10 numbers
    print("\n")


def job_4_fizzbuzz() -> None:
    """Job 4: Classic FizzBuzz problem.
    
    Demonstrates: Multiple elif conditions and modulo operator.
    """
    print("FizzBuzz (0-100):")
    for x in range(100):
        if x == 0:
            continue
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz", end=" ")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        elif x % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(x, end=" ")
    print("\n")


def est_premier(num: int) -> bool:
    """Check if a number is prime.
    
    Args:
        num: Number to check for primality.
        
    Returns:
        True if number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def job_5_prime_numbers() -> None:
    """Job 5: Find all prime numbers in a range.
    
    Demonstrates: Function definition, loops, and conditional logic.
    """
    primes = [num for num in range(PRIME_RANGE_START, PRIME_RANGE_END + 1) if est_premier(num)]
    
    print(f"Prime numbers between {PRIME_RANGE_START} and {PRIME_RANGE_END}:")
    print(f"Found {len(primes)} primes:")
    for i, prime in enumerate(primes, 1):
        print(prime, end=" ")
        if i % 10 == 0:
            print()
    print("\n")


def job_6_even_odd_checker() -> None:
    """Job 6: Determine if a number is even or odd.
    
    Demonstrates: Modulo operator and f-string formatting.
    """
    try:
        nombre = int(input("Veuillez entrer un nombre: "))
        if nombre % 2 == 0:
            print(f"✓ Le nombre {nombre} est pair")
        else:
            print(f"✓ Le nombre {nombre} est impair")
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")


def job_7_string_pyramid() -> None:
    """Job 7: Build a pyramid pattern from string input.
    
    Demonstrates: String slicing and nested loop logic.
    """
    chaine = input("Veuillez entrer une chaîne de caractères: ")
    
    if len(chaine) == 0:
        print("⚠ Chaîne vide. Impossible de créer une pyramide.")
        return
    
    print("Pyramide créée:")
    index = 0
    for i in range(1, MAX_PYRAMID_LINES + 1):
        if index + i <= len(chaine):
            print(chaine[index:index + i])
            index += i
        else:
            break


def est_constructible(a: float, b: float, c: float) -> bool:
    """Check if three sides can form a valid triangle.
    
    Args:
        a, b, c: Lengths of triangle sides.
        
    Returns:
        True if sides can form a valid triangle, False otherwise.
    """
    return a + b > c and a + c > b and b + c > a


def type_de_triangle(a: float, b: float, c: float) -> str:
    """Determine the type of triangle from side lengths.
    
    Args:
        a, b, c: Lengths of triangle sides (assumed valid).
        
    Returns:
        String describing triangle type: 'équilatéral', 'isocèle', 
        'rectangle isocèle', 'rectangle', or 'scalène'.
    """
    if a == b == c:
        return "équilatéral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "rectangle isocèle"
        return "isocèle"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "rectangle"
    else:
        return "scalène"


def job_8_triangle_validator() -> None:
    """Job 8: Validate and classify triangles.
    
    Demonstrates: Function composition and triangle geometry validation.
    """
    try:
        a = float(input("Entrez le côté a: "))
        b = float(input("Entrez le côté b: "))
        c = float(input("Entrez le côté c: "))
        
        if a <= 0 or b <= 0 or c <= 0:
            print("⚠ Les côtés doivent être positifs")
            return

        if est_constructible(a, b, c):
            triangle_type = type_de_triangle(a, b, c)
            print(f"✓ Triangle valide: {triangle_type}")
        else:
            print("✗ Triangle non constructible (inégalité triangulaire violée)")
    except ValueError:
        print("⚠ Veuillez entrer des nombres valides")


# Job registry for menu system
JOBS = {
    "1": ("Comparer deux valeurs", job_1_compare_values),
    "2": ("Vérifier l'âge de vote", job_2_voting_eligibility),
    "3": ("Boucle avec continue (0-100)", job_3_skip_numbers),
    "4": ("FizzBuzz classique", job_4_fizzbuzz),
    "5": ("Trouver les nombres premiers", job_5_prime_numbers),
    "6": ("Vérifier pair/impair", job_6_even_odd_checker),
    "7": ("Pyramide de chaîne", job_7_string_pyramid),
    "8": ("Validateur de triangle", job_8_triangle_validator),
}
