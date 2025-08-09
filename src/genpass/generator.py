from .complexity import ComplexityLevel, SimpleComplexityStrategy, MediumComplexityStrategy, HighComplexityStrategy



class PasswordGenerator:
    """
    A class to generate passwords based on specified complexity and length.
    """
    @staticmethod
    def generate_password(lowercase_length, uppercase_length, complexity):
        if complexity == ComplexityLevel.SIMPLE:
            return SimpleComplexityStrategy.generate_password(lowercase_length)
        elif complexity == ComplexityLevel.MEDIUM:
            return MediumComplexityStrategy.generate_password(lowercase_length, uppercase_length)
        elif complexity == ComplexityLevel.HIGH:
            return HighComplexityStrategy.generate_password(lowercase_length, uppercase_length)
        return None
