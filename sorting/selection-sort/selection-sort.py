"""
    ? Problem Statement: Selection Sort.
    
    ! Time Complexity: O(n^2)
    ! Space Complexity: O(1)
"""

def selectionSort(arr: list[int]) -> None:
    for i in range(len(arr) - 1):
        smallest_index = i
        
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                
        if i != smallest_index:
            [arr[i], arr[smallest_index]] = [arr[smallest_index], arr[i]]
            
            
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
selectionSort(nums)
print(nums)