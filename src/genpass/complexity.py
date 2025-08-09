import string
import random

from abc import ABC, abstractmethod


class ComplexityLevel:
    SIMPLE = 'SIMPLE'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    COMPLEXITY_LIST = [SIMPLE, MEDIUM, HIGH]


class ComplexityStrategy(ABC):
    @staticmethod
    @abstractmethod
    def generate_password(lowercase_length, uppercase_length):
        pass


class SimpleComplexityStrategy(ComplexityStrategy):
    @staticmethod
    def generate_password(lowercase_length, uppercase_length=None):
        all_characters = ''.join(string.ascii_lowercase)
        result = ''.join(random.choice(all_characters)
                         for _ in range(lowercase_length))
        return result


class MediumComplexityStrategy(ComplexityStrategy):
    @staticmethod
    def generate_password(lowercase_length, uppercase_length):
        lowercase_random_chars = ''.join(random.choice(
            string.ascii_lowercase) for _ in range(lowercase_length))
        uppercase_random_chars = ''.join(random.choice(
            string.ascii_uppercase) for _ in range(uppercase_length))
        result = ''.join(random.sample(
            lowercase_random_chars + uppercase_random_chars, lowercase_length + uppercase_length))
        return result


class HighComplexityStrategy(ComplexityStrategy):
    @staticmethod
    def generate_password(lowercase_length, uppercase_length):
        random_digit = ''.join(random.choice(string.digits) for _ in range(1))
        random_special_char = ''.join(random.choice(
            string.punctuation) for _ in range(1))
        lowercase_random_chars = ''.join(random.choice(
            string.ascii_lowercase) for _ in range(lowercase_length))
        uppercase_random_chars = ''.join(random.choice(
            string.ascii_uppercase) for _ in range(uppercase_length))
        all_characters = lowercase_random_chars + \
            uppercase_random_chars + random_digit + random_special_char
        result = ''.join(random.sample(all_characters, len(all_characters)))
        return result
