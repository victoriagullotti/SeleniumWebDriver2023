#   Just some method
import pytest


def add_two_numbers(a, b):
    return a + b

#   Test small numbers
@pytest.mark.math_old
def test_small_numbers():
    assert add_two_numbers(1, 6) == 7, "The sum of 1 and 6 should be 7."

#   Test large numbers
@pytest.mark.math_old
def test_large_numbers():
    assert add_two_numbers(1000, 9000) == 10000, "The sum of 1000 and 9000 should be 10000."

#   Calling tests
#test_small_numbers()
#test_large_numbers()
