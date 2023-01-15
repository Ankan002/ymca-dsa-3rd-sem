"""
    ? Problem Statement: Heap Sort.
    
    ! Time Complexity: O(n log n)
    ! Space Complexity: O(1)
"""

def maxHeapify(nums: list[int], parentIndex: int, maxLength: int) -> None:
    if parentIndex > maxLength: return
    
    leftChildIndex = (parentIndex * 2) + 1
    rightChildIndex = (parentIndex * 2) + 2
    currentLargestIndex = parentIndex
    
    if leftChildIndex <= maxLength and nums[leftChildIndex] > nums[currentLargestIndex]: currentLargestIndex = leftChildIndex
    
    if rightChildIndex <= maxLength and nums[rightChildIndex] > nums[currentLargestIndex]: currentLargestIndex = rightChildIndex
    
    if currentLargestIndex != parentIndex:
        nums[parentIndex], nums[currentLargestIndex] = nums[currentLargestIndex], nums[parentIndex]
        maxHeapify(nums, currentLargestIndex, maxLength)
        
def convertToMaxHeap(nums: list[int]) ->  None:
    maxLength = len(nums) - 1
    currentParentIndex = maxLength // 2
    
    while currentParentIndex >= 0:
        maxHeapify(nums, currentParentIndex, maxLength)
        currentParentIndex -= 1
        
def maxHeapPop(nums: list[int]) -> None:
    lastIndex = len(nums) - 1
    
    while lastIndex != 0:
        nums[0], nums[lastIndex] = nums[lastIndex], nums[0]
        maxHeapify(nums, 0, lastIndex - 1)
        lastIndex -= 1
        
def heapSort(nums: list[int]) -> None:
    convertToMaxHeap(nums)
    maxHeapPop(nums)
    
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
heapSort(nums)
print(nums)       
