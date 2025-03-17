import pytest
from commenter.parser import insert_docstrings_in_code

def test_insert_docstring():
    #Sample output docstring
    input_code = """
def add(a, b):
    return a + b
"""

    expected_code = """
def add(a, b):
    \"\"\"Adds two numbers and returns the sum.\"\"\"
    return a + b
"""

    output_code = insert_docstrings_in_code(input_code)

    assert "Return the sum of two numbers." in output_code
    assert "Parameters:" in output_code
    assert "Returns:" in output_code
