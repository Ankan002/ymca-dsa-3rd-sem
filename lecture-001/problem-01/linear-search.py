"""
    ? Problem Statement: Q1 of Lecture 01 Problems.

    ! Time Complexity: O(n)
    ! Space Complexity: O(1)
"""

def linear_search(nums: list[int], key: int) -> int:
    for i in range(len(nums)):
        if nums[i] == key:
            return i

    return -1

print(linear_search([1, 3, 5, 4, 7, 9], 7))
print(linear_search([1, 3, 5, 4, 7, 9], 9))
print(linear_search([1, 3, 5, 4, 7, 9], 1))
print(linear_search([1, 3, 5, 4, 7, 9], 10))
