from .complexity import ComplexityLevel


class AlphaCharacterDistribution:
    def __init__(self, uppercase_length, lowercase_length):
        self.uppercase_length = uppercase_length
        self.lowercase_length = lowercase_length


class CharacterDistributionCalculator:
    @staticmethod
    def get_upper_lower_case_length_by_complexity(complexity, length):
        if complexity == ComplexityLevel.SIMPLE:
            return AlphaCharacterDistribution(0, length)
        elif complexity == ComplexityLevel.MEDIUM:
            if length % 2 == 0:
                return AlphaCharacterDistribution(length // 2, length // 2)
            else:
                uppercase_length = sum(divmod(length, 2))
                lowercase_length = length - uppercase_length
                return AlphaCharacterDistribution(uppercase_length, lowercase_length)
        elif complexity == ComplexityLevel.HIGH:
            alpha_length = length - 2
            if alpha_length % 2 != 0:
                uppercase_length = sum(divmod(alpha_length, 2))
                lowercase_length = alpha_length - uppercase_length
                return AlphaCharacterDistribution(uppercase_length, lowercase_length)
            return AlphaCharacterDistribution(alpha_length // 2, alpha_length // 2)
        else:
            raise ValueError("Invalid complexity level provided.")