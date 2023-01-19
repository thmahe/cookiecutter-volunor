import textwrap

from volunor.test.mock import with_captured_output, with_arguments, with_exit_code, CliTestCase

from {{ cookiecutter.package_name }}.cli import descriptor as cli_descriptor


class TestCommand(CliTestCase):

    descriptor = cli_descriptor

    @with_exit_code(exit_code=0)
    @with_captured_output()
    @with_arguments('-h')
    def test_greet_helper(self):
        self.expected_output = textwrap.dedent("""\
        usage: TestCommand [-h] COMMAND ...
        
        optional arguments:
          -h, --help  show this help message and exit
        
        commands:
          greet .... Simple greet command
        """)

        self.cli.big_bang()

    @with_exit_code(exit_code=0)
    @with_captured_output()
    @with_arguments('greet', 'cookiecutter-volunor', '--count', '2')
    def test_greet_command(self):
        self.expected_output = textwrap.dedent("""\
        Hello cookiecutter-volunor
        Hello cookiecutter-volunor
        """)

        self.cli.big_bang()
