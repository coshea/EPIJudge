from test_framework import generic_test


def is_well_formed(s):
    left_stack = []
    left_brackets = {'(': ')',
                     '[': ']',
                     '{': '}'}
    right_brackets = {')': '(',
                      ']': '[',
                      '}': '{'}

    for c in s:
        if c in left_brackets:
            left_stack.append(left_brackets[c])
        elif c in right_brackets:
            if len(left_stack) == 0:
                return False
            if left_stack.pop() != c:
                return False

    return len(left_stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
