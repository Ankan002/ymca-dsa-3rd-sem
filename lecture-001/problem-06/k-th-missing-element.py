"""
    ? Problem Statement: Q6 of lecture 1
    ! Time Complexity: O(log n)
    ! Space Complexity: O(1)
"""

def solve(arr: list[int],  k: int) -> int:
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] - mid - 1 < k:
            left = mid + 1
        else:
            right = mid - 1
            
    return right + k
 
 
arr = [2, 3, 5, 9, 10, 11, 12]
print(solve(arr, 4))