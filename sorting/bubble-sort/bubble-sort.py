"""
    ? Problem Statement: Bubble Sort.
    
    ! Time Complexity: O(n^2)
    ! Space Complexity: O(1)
"""

def bubble_sort(nums: list[int]) -> None:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
            
            
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
bubble_sort(nums)
print(nums)