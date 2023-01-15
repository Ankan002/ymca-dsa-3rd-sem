"""
    ? Problem Statement: Merge Sort.
    
    ! Time Complexity: O(n^2)
    ! Space Complexity: O(1)
"""

def partition(nums: list[int], lb: int, ub: int) -> int:
    pivot = nums[lb]
    
    i = lb
    
    for j in range(i+1, ub+1):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i], nums[lb] = nums[lb], nums[i]
    
    return i

def quickSort(nums: list[int], lb: int, ub: int) -> None:
    if lb < ub:
        pivot = partition(nums, lb, ub)
        
        quickSort(nums, lb, pivot - 1)
        quickSort(nums, pivot + 1, ub)
 
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
quickSort(nums, 0, len(nums) - 1)
print(nums)   
    