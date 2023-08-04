"""
----------Introduction to Property-Based Testing:------------------
Using Hypothesis package

Unit Test: Fixture of specific input values and executes tests with
    that fixture and asserts that result is as expected
Property Test: Checks that a function abides by a property. Not focused
    on inputs and outputs, just check specific characteristics.
    Automatically generate example input data.
    Properties examples:
        In an encode-decode program, you can check the operation and the
        reverse operation to see if it works properly.
        Properties of data, like if a sorting algorithm does not alter
        the length of the list.
        Check is a function adheres to some condition. For example, in a
        function that generates UUIDs, you can check if the generated id
        follows the UUID structure

"""
from functools import reduce


def to_ascii_codes(inp: str) -> list[int]:
    return [ord(c) for c in inp]


def from_ascii_codes(inp: list[int]) -> str:
    return reduce(lambda x, y: x + chr(y), inp, "")
