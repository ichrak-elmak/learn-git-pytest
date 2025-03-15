from ..string_utils import reverse_string, count_vowels, is_palindrome, capitalize_words
import pytest
def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_count_vowels():
    assert count_vowels("hello") == 2

def test_is_palindrome():
    assert is_palindrome("racecar") == True

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"