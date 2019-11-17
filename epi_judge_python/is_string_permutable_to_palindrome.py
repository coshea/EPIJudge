from test_framework import generic_test
from collections import Counter

# 12.1
# Leetcode #266 - Palindrome Permutation


def can_form_palindrome_book(s):
    return sum(v % 2 for v in Counter(s).values()) <= 1


def can_form_palindrome_mine(s):
    _set: set = set()
    _dict: dict = {}

    for c in s:
        if c in _set:
            _set.remove(c)
        else:
            _set.add(c)

    if len(s) % 2 == 1 and len(_set) == 1:
        return True
    if len(s) % 2 == 0 and len(_set) == 0:
        return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome_mine))
