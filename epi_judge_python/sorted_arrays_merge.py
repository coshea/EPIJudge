from test_framework import generic_test
from typing import List
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]):
    """
    EPI 10.1 Merge sorted files. Page 143
    """
    min_heap: List[Tuple[int, int]] = []
    # Build a list of iterators for each array in sorted_arrays.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap
    for counter, it in enumerate(sorted_arrays_iters):
        first_element = next(it)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, counter))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)

        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
