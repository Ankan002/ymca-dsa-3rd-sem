"""
    ? Problem Statement: Q3 of Lecture 01 Problems.

    ! Time Complexity: O(n)
    ! Space Complexity: O(1)
"""


def find_frequency(nums: list[int], key: int) -> int:
    frequency = 0

    for num in nums:
        if num == key:
            frequency += 1

    return frequency


print(find_frequency([10, 20, 20, 10, 10, 20, 5, 20], 20))
print(find_frequency([10, 20, 20, 10, 10, 20, 5, 20], 10))
