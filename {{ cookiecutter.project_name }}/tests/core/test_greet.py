import contextlib
import io
import textwrap
from unittest import TestCase

from {{ cookiecutter.package_name }}.core.greet import greet


class TestCore(TestCase):

    def test_greet(self):
        expected_output = textwrap.dedent("""\
        Hello cookiecutter-volunor
        Hello cookiecutter-volunor
        """)
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            greet(name="cookiecutter-volunor", count=2)

        self.assertEqual(expected_output, captured.getvalue())
