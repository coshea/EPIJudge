from test_framework import generic_test


def is_palindrome(s):
    """
    Leetcode #125 - Valid Palindrome I
    """
    start, end = 0, len(s)-1

    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True


def is_palindrome_skip_one_letter(self, s: str) -> bool:
    """
    Leetcode #680 - Valid Palindrome II
    """
    left, right = 0, len(s)-1

    while(left < right):
        if s[left] != s[right]:
            skip_right = s[left:right]  # take left to right(not inclusive)
            skip_left = s[left+1:right+1]  # take left+1 to right(inclusive)

            return (skip_right == skip_right[:: -1]
                    or skip_left == skip_left[::-1])
        left, right = left + 1, right - 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
