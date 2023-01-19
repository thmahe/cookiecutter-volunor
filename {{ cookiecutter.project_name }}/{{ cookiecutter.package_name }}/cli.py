from volunor import Cli

from {{ cookiecutter.package_name }}.commands.greet import GreetCommand

descriptor = {
    "greet": GreetCommand
}

cli = Cli(descriptor, prog="{{cookiecutter.prog_name}}")

def entry_point():
    cli.big_bang()

if __name__ == '__main__':
    entry_point()

