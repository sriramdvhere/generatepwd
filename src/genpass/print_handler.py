import click

class PrintHandler:

    @staticmethod
    def print_error(error):
        click.echo(click.style(f"Error: {error}", fg='red'))

    @staticmethod
    def print_password(password):
        click.echo(click.style(f"Generated Password: {password}", fg='green'))

    @staticmethod
    def print_complexity_help():
        click.echo(click.style(
            "Complexity Levels:\n"
            "SIMPLE: Only lowercase letters.\n"
            "MEDIUM: Equal mix of uppercase and lowercase letters.\n"
            "HIGH: Mix of uppercase, lowercase, digits, and special characters.",
            fg='blue'))
