import pytest
from my_module import hyphenate_strings # Import the function

def test_hyphenate_strings_basic():
  assert hyphenate_strings("hello", "world") == "hello-world"

def test_hyphenate_strings_different_cases():
  assert hyphenate_strings("Python", "code") == "Python-code"
  assert hyphenate_strings("UPPER", "lower") == "UPPER-lower"

def test_hyphenate_strings_empty_string_first():
  assert hyphenate_strings("", "test") == "-test"

def test_hyphenate_strings_empty_string_second():
  assert hyphenate_strings("test", "") == "test-"

def test_hyphenate_strings_both_empty():
  assert hyphenate_strings("", "") == "-"

def test_hyphenate_strings_numbers():
    assert hyphenate_strings("123", "456") == "123-456"

def test_hyphenate_strings_special_characters():
    assert hyphenate_strings("!@#", "$%^") == "!@#-$%^"
