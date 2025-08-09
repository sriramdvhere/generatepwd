
from abc import ABC, abstractmethod

from .password_exceptions import InvalidComplexityException, InvalidLengthException
from .complexity import ComplexityLevel


class Validator(ABC):
    @staticmethod
    @abstractmethod
    def validate(value):
        pass


class ComplexityValidator(Validator):
    @staticmethod
    def validate(complexity):
        if not any(True for item in ComplexityLevel.COMPLEXITY_LIST if complexity == item):
            raise InvalidComplexityException()
        if not complexity:
            raise InvalidComplexityException(
                "Complexity cannot be an empty list.")


class LengthValidator(Validator):
    @staticmethod
    def validate(length):
        if not isinstance(length, int):
            raise InvalidLengthException("Length must be an integer.")
        if length <= 0:
            raise InvalidLengthException("Length must be a positive integer.")
        if length > 100:
            raise InvalidLengthException()
