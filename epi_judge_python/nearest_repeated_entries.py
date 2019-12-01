from test_framework import generic_test
from typing import List


def find_nearest_repetition(paragraph: List[str]) -> int:
    """
    EPI 12.5 Nearest repeated entries in an array
    """
    words: Dict[str, int] = {}
    min_dist = float('inf')

    for i, word in enumerate(paragraph):
        if word not in words:
            words[word] = i
        else:
            dist = i - words[word]
            min_dist = min(dist, min_dist)
            words[word] = i

    return min_dist if min_dist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
