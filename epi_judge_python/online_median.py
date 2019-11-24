from test_framework import generic_test
import heapq
from typing import List, Iterator


def online_median(sequence: Iterator[int]) -> List[float]:
    """
    EPI 10.5 Online Median. Page 148
    """

    # min heap to keep left values, max heap to keep right values
    min_heap: List[int] = []
    max_heap: List[int] = []
    result = []
    for s in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, s))

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(max_heap) == len(min_heap):
            result.append(((max_heap[0] * -1) + min_heap[0]) / 2)
        else:
            result.append(min_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
