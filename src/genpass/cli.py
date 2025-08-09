"""CLI module for genpass: handles input parsing and command execution."""

import click

from .password_exceptions import PasswordGenerationException
from .print_handler import PrintHandler
from .validators import LengthValidator, ComplexityValidator
from .distribution import CharacterDistributionCalculator
from .generator import PasswordGenerator


def validate_input(length, complexity):
    """Validate length and complexity inputs.

    Args:
        length (int): Desired password length.
        complexity (str): Desired complexity level.

    Returns:
        bool: True if inputs are valid, False otherwise.
    """
    try:
        ComplexityValidator.validate(complexity)
        LengthValidator.validate(length)
    except PasswordGenerationException as e:
        PrintHandler.print_error(e)
        PrintHandler.print_complexity_help()
        return False
    return True


@click.command()
@click.option('-l', '--length', default=12, help='Length of the password to be generated.')
@click.option(
    '-c', '--complexity', default='SIMPLE',
    help=(
        '''Provide any Complexity level option from SIMPLE, MEDIUM, HIGH of the password.
        Complexity Levels:
        SIMPLE: Only lowercase letters.
        MEDIUM: Equal mix of uppercase and lowercase letters.
        HIGH: Mix of uppercase, lowercase, digits, and special characters.
        Default is SIMPLE.'''
    )
)
def genpass(length=12, complexity='SIMPLE'):
    """CLI command to generate a password.

    Args:
        length (int): Length of the password (default: 12).
        complexity (str): Complexity level: SIMPLE, MEDIUM, or HIGH (case-insensitive).
    """

    complexity = complexity.upper()

    if not validate_input(length, complexity):
        return

    character_distribution = CharacterDistributionCalculator.get_upper_lower_case_length_by_complexity(
        complexity, length)
    uppercase_length = character_distribution.uppercase_length
    lowercase_length = character_distribution.lowercase_length

    result = PasswordGenerator.generate_password(
        lowercase_length, uppercase_length, complexity)

    if not result:
        PrintHandler.print_error("Password generation failed.")
        return

    PrintHandler.print_password(result)
