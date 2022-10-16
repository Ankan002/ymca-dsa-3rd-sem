"""
    ? Problem Statement: Q2 of Lecture 01 Problems.

    ! Time Complexity: O(log n)
    ! Space Complexity: O(1)
"""


def binary_search(nums: list[int], key: int) -> int:
    lb = 0
    ub = len(nums) - 1

    while lb <= ub:
        mid = lb + ((ub - lb) // 2)

        if nums[mid] == key: return mid
        elif nums[mid] > key: ub = mid - 1
        else: lb = mid + 1

    return -1


print(binary_search([10, 20, 30, 40, 50, 60, 70], 70))
print(binary_search([10, 20, 30, 40, 50, 60, 70], 20))
print(binary_search([10, 20, 30, 40, 50, 60, 70], 10))
print(binary_search([10, 20, 30, 40, 50, 60, 70], 100))
print(binary_search([10, 20, 30, 40, 50, 60, 70], 0))
