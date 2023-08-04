from ..ascii import from_ascii_codes, to_ascii_codes
from hypothesis import given, example, settings
from hypothesis.strategies import text


# test the correct functionality of the functions
@given(text())  # generates random texts
@example("")  # make sure to include certain examples in test
@settings(max_examples=100)  # maximum examples you want to generate
def test_decode_inverts_encode(test_str: str) -> None:
    assert from_ascii_codes(to_ascii_codes(test_str)) == test_str


# test that the length of input == length of output
@given(text())
def test_list_length_same_as_input_str(test_str: str) -> None:
    encoded = to_ascii_codes(test_str)
    assert len(encoded) == len(test_str)
