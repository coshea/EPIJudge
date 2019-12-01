from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import OrderedDict
import typing


class LruCache:
    """
    EPI 12.3 Implement an LRU Cache
    Leetcode #146 https://leetcode.com/problems/lru-cache/
    """

    def __init__(self, capacity):
        self._capacity = capacity
        self._ordered_table: OrderedDict[int, int] = OrderedDict()

    def lookup(self, isbn) -> int:
        if isbn not in self._ordered_table:
            return -1

        price = self._ordered_table.pop(isbn)  # Get item, remove from dict
        self._ordered_table[isbn] = price  # re-add item at back of queue
        return price

    def insert(self, isbn, price) -> None:
        if isbn in self._ordered_table:
            price = self._ordered_table.pop(isbn)  # Get item, remove from dict
        elif len(self._ordered_table) == self._capacity:
            self._ordered_table.popitem(False)

        self._ordered_table[isbn] = price  # re-add item at back of queue

    def erase(self, isbn) -> bool:
        return self._ordered_table.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
