"""Unit tests for Python Day 3 exercises."""

import pytest
from jobs import (
    est_premier,
    est_constructible,
    type_de_triangle,
)


class TestPrimeNumbers:
    """Test cases for prime number checker."""
    
    def test_est_premier_small_primes(self):
        """Test small prime numbers."""
        assert est_premier(2) is True
        assert est_premier(3) is True
        assert est_premier(5) is True
        assert est_premier(7) is True
    
    def test_est_premier_non_primes(self):
        """Test non-prime numbers."""
        assert est_premier(0) is False
        assert est_premier(1) is False
        assert est_premier(4) is False
        assert est_premier(6) is False
        assert est_premier(8) is False
        assert est_premier(9) is False
    
    def test_est_premier_negative(self):
        """Test negative numbers (not prime)."""
        assert est_premier(-1) is False
        assert est_premier(-5) is False
    
    def test_est_premier_large_primes(self):
        """Test larger prime numbers."""
        assert est_premier(97) is True
        assert est_premier(101) is True
        assert est_premier(997) is True
    
    def test_est_premier_large_composites(self):
        """Test larger composite numbers."""
        assert est_premier(100) is False
        assert est_premier(121) is False  # 11 * 11
        assert est_premier(143) is False  # 11 * 13


class TestTriangleValidator:
    """Test cases for triangle validation and classification."""
    
    def test_est_constructible_equilateral(self):
        """Test equilateral triangle validity."""
        assert est_constructible(3, 3, 3) is True
    
    def test_est_constructible_isosceles(self):
        """Test isosceles triangle validity."""
        assert est_constructible(5, 5, 6) is True
    
    def test_est_constructible_scalene(self):
        """Test scalene triangle validity."""
        assert est_constructible(3, 4, 5) is True
    
    def test_est_constructible_invalid(self):
        """Test invalid triangle (violates triangle inequality)."""
        assert est_constructible(1, 2, 5) is False
        assert est_constructible(1, 1, 2) is False  # Degenerate case
    
    def test_est_constructible_edge_cases(self):
        """Test edge cases."""
        assert est_constructible(0.1, 0.1, 0.1) is True
        assert est_constructible(1, 1, 1.9) is True
        assert est_constructible(1, 1, 2) is False  # Degenerate
    
    def test_type_de_triangle_equilateral(self):
        """Test equilateral triangle classification."""
        assert type_de_triangle(5, 5, 5) == "équilatéral"
        assert type_de_triangle(1, 1, 1) == "équilatéral"
    
    def test_type_de_triangle_isosceles(self):
        """Test isosceles triangle classification."""
        assert type_de_triangle(5, 5, 6) == "isocèle"
        assert type_de_triangle(7, 7, 10) == "isocèle"
    
    def test_type_de_triangle_rectangle(self):
        """Test right triangle (Pythagorean theorem)."""
        # 3-4-5 triangle
        assert type_de_triangle(3, 4, 5) == "rectangle"
        # 5-12-13 triangle
        assert type_de_triangle(5, 12, 13) == "rectangle"
    
    def test_type_de_triangle_scalene(self):
        """Test scalene triangle classification."""
        assert type_de_triangle(3, 4, 6) == "scalène"
        assert type_de_triangle(2, 3, 4) == "scalène"


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_prime_count_in_range(self):
        """Test counting primes in a range."""
        primes = [n for n in range(2, 101) if est_premier(n)]
        # There are 25 primes between 2 and 100
        assert len(primes) == 25
    
    def test_triangle_validation_workflow(self):
        """Test complete triangle validation workflow."""
        # Valid right triangle
        assert est_constructible(3, 4, 5) is True
        assert type_de_triangle(3, 4, 5) == "rectangle"
        
        # Invalid triangle
        assert est_constructible(1, 2, 5) is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
