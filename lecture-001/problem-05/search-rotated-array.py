"""
    ? Problem Statement: Q5 of lecture 1
    
    ! Time Complexity: O(log n)
    ! Space Complexity: O(1)
"""

def searchInRotatedArray(rotatedArray: list[int], target: int) -> int:
    leftIndex = 0
    rightIndex = len(rotatedArray) - 1
    
    while leftIndex <= rightIndex:
        midIndex = leftIndex + ((rightIndex - leftIndex) // 2)
        
        if rotatedArray[midIndex] == target: return midIndex
        
        elif rotatedArray[midIndex] >= rotatedArray[leftIndex] and target < rotatedArray[midIndex] and target >= rotatedArray[leftIndex]: rightIndex = midIndex - 1
        
        elif rotatedArray[midIndex] <= rotatedArray[rightIndex] and target > rotatedArray[midIndex] and target <= rotatedArray[rightIndex]: leftIndex = midIndex + 1
        
        elif rotatedArray[midIndex] >= rotatedArray[rightIndex]: leftIndex = midIndex + 1
        
        elif rotatedArray[midIndex] <= rotatedArray[leftIndex]: rightIndex = midIndex - 1
        
        else: return -1
              
    return -1

print(searchInRotatedArray([4,5,6,7,0,1,2], 0))
print(searchInRotatedArray([4,5,6,7,0,1,2], 3))
print(searchInRotatedArray([1, 3, 5], 5))