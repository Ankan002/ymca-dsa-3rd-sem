"""
    ? Problem Statement: Merge Sort.
    
    ! Time Complexity: O(n log n)
    ! Space Complexity: O(n)
"""

def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    tempList: list[int] = []

    arrayOnePos = left
    arrayTwoPos = mid + 1

    while arrayOnePos <= mid and arrayTwoPos <= right:
        if arr[arrayOnePos] <= arr[arrayTwoPos]:
            tempList.append(arr[arrayOnePos])
            arrayOnePos += 1
        else:
            tempList.append(arr[arrayTwoPos])
            arrayTwoPos += 1
            
    while arrayOnePos <= mid:
        tempList.append(arr[arrayOnePos])
        arrayOnePos += 1
        
    while arrayTwoPos <= right:
        tempList.append(arr[arrayTwoPos])
        arrayTwoPos += 1
        
    currentReplacePosition = left
    
    for num in tempList:
        arr[currentReplacePosition] = num
        currentReplacePosition += 1
        
def divide(arr: list[int], left: int, right: int) -> None:
    if left < right:
        mid = left + ((right - left) // 2)
        
        divide(arr, left, mid)
        divide(arr, mid+1, right)
        merge(arr, left, mid, right)
        
    return
        
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
divide(nums, 0, len(nums) - 1)
print(nums)
