"""
    ? Problem Statement: Q3 of Lecture 01 Problems.

    ! Time Complexity: O(log n)
    ! Space Complexity: O(1)
"""

def findStartIndex(nums: list[int], key: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        midIndex = left + ((right - left) // 2)
        
        if nums[midIndex] == key and (midIndex == 0 or nums[midIndex - 1] != key): return midIndex
        
        elif nums[midIndex] >= key: right = midIndex - 1
        
        else: left = midIndex + 1
        
    return -1

def findLastIndex(nums: list[int], key: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        midIndex = left + ((right - left) // 2)
        
        if nums[midIndex] == key and (midIndex == len(nums) - 1 or nums[midIndex + 1] != key): return midIndex
        
        elif nums[midIndex] <= key: left = midIndex + 1
        
        else: right = midIndex - 1
        
    return -1

def find_frequency(nums: list[int], key: int) -> int: 
    startIndex = findStartIndex(nums, key)
    if startIndex == -1: return -1
    
    lastIndex = findLastIndex(nums, key)
    if lastIndex == -1: return -1
    
    return (lastIndex - startIndex) + 1


print(find_frequency([1, 1, 2, 2, 2, 2, 3], 2))
print(find_frequency([1, 1, 2, 2, 2, 2, 3], 3))
print(find_frequency([1, 1, 2, 2, 2, 2, 3], 1))
print(find_frequency([1, 1, 2, 2, 2, 2, 3], 4))
