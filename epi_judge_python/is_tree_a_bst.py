from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
