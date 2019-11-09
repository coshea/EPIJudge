from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple

# 8.1
class Stack:
    ElementWithMax = namedtuple('ElementWithMax', ('element', 'max'))
    
    def __init__(self) -> None:
        self._stack_with_max: List[Stack.ElementWithMax] = []
    
    def empty(self):        
        return len(self._stack_with_max) == 0

    def max(self):        
        return self._stack_with_max[-1].max

    def pop(self):        
        return self._stack_with_max.pop().element

    def push(self, x):
        self._stack_with_max.append(self.ElementWithMax(x, x if self.empty() else max(x, self.max())))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
