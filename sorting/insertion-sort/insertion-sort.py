"""
    ? Problem Statement: Insertion Sort.
    
    ! Time Complexity: O(n^2)
    ! Space Complexity: O(1)
"""

def insertionSort(nums: list[int]) -> None:
    for i in range(len(nums) - 1):
        compareNum = nums[i+1]
        currentComparingIndex = i
        
        while currentComparingIndex >= 0 and nums[currentComparingIndex] > compareNum:
            nums[currentComparingIndex + 1] = nums[currentComparingIndex]
            currentComparingIndex -= 1
            
        nums[currentComparingIndex + 1] = compareNum
        
        
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
insertionSort(nums)
print(nums)