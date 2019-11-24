from test_framework import generic_test
from binary_tree_node import BinaryTreeNode
from collections import deque, namedtuple


def is_binary_tree_bst(tree: BinaryTreeNode, low_range=float('-inf'), high_range=float('inf')):
    """
    EPI 14.1 Test if BST. Page 214
    """
    if not tree:
        return True

    if not low_range <= tree.data <= high_range:
        return False

    return (is_binary_tree_bst(tree.left, low_range, tree.data)
            and is_binary_tree_bst(tree.right, tree.data, high_range))


def is_binary_tree_bst_queue(tree: BinaryTreeNode, low_range=float('-inf'), high_range=float('inf')):
    """
    EPI 14.1 Test if BST. Page 214
    """
    if not tree:
        return True

    QueueEntry = namedtuple('QueueEntry', ('node', 'lower', 'higher'))

    bfs_queue = deque([QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        item = bfs_queue.popleft()

        if not item.lower <= item.node.data <= item.higher:
            return False

        bfs_queue.extend(
            QueueEntry(item.node.left, item.lower, item.node.data))
        bfs_queue.append(
            QueueEntry(item.node.right, item.node.data, item.higher))

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_queue))
