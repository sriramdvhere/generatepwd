"""Module for password generation logic based on complexity strategies."""
from .complexity import (ComplexityLevel, HighComplexityStrategy,
                         MediumComplexityStrategy, SimpleComplexityStrategy)


def generate_password(lowercase_length, uppercase_length, complexity):
    """Generate a password string.

    Args:
        lowercase_length (int): Number of lowercase characters.
        uppercase_length (int): Number of uppercase characters.
        complexity (str): Complexity level (SIMPLE, MEDIUM, HIGH).

    Returns:
        str or None: Generated password if successful, None otherwise.
    """
    if complexity == ComplexityLevel.SIMPLE:
        return SimpleComplexityStrategy.generate_password(lowercase_length)
    if complexity == ComplexityLevel.MEDIUM:
        return MediumComplexityStrategy.generate_password(lowercase_length, uppercase_length)
    if complexity == ComplexityLevel.HIGH:
        return HighComplexityStrategy.generate_password(lowercase_length, uppercase_length)
    return None
