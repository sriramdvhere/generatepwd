"""Unit tests of generatepwd: unit tests of password generation."""

from generatepwd.generator import generate_password
from generatepwd.complexity import ComplexityLevel


def test_simple_password_generation():
    """Test password generation with SIMPLE complexity."""
    password_simple = generate_password(5, 0, ComplexityLevel.SIMPLE)
    assert isinstance(password_simple, str)
    assert len(password_simple) == 5
    assert password_simple.islower()


def test_medium_password_generation():
    """Test password generation with MEDIUM complexity."""
    password_medium = generate_password(3, 2, ComplexityLevel.MEDIUM)
    assert isinstance(password_medium, str)
    assert len(password_medium) == 5
    assert sum(1 for c in password_medium if c.islower()) == 3
    assert sum(1 for c in password_medium if c.isupper()) == 2


def test_high_password_generation():
    """Test password generation with HIGH complexity."""

    password_high = generate_password(3, 2, ComplexityLevel.HIGH)
    assert isinstance(password_high, str)
    assert len(password_high) == (5+2)
    assert sum(1 for c in password_high if c.islower()) == 3
    assert sum(1 for c in password_high if c.isupper()) == 2


def test_invalid_password_generation():
    """Test invalid complexity"""
    invalid_password = generate_password(5, 0, "INVALID")
    assert invalid_password is None
