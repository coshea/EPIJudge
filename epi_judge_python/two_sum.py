from test_framework import generic_test


def has_two_sum(nums, target: int):
    sums = {}
    result = []

    for i in range(len(nums)):
        # because you can use same number twice, check not in first
        # differs from leetcode problem
        if not nums[i] in sums:
            sums[target-nums[i]] = i

        if nums[i] in sums:
            result.append(sums[nums[i]])
            result.append(nums[i])
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
