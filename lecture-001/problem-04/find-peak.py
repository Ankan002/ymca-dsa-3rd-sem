def find_peak(nums: list[int]) -> int:
    if len(nums) <= 0: return -1
    if len(nums) == 1: return nums[1]
    
    left = 0
    right = len(nums) - 1
    
    while(left <= right):
        mid = left + ((right - left) // 2)
        
        if mid == 0 and nums[mid + 1] < nums[mid]: return nums[mid]
        elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]: return nums[mid]
        elif nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]: return nums[mid]
        
        elif nums[mid - 1] > nums[mid]: right = mid - 1
        elif nums[mid + 1] > nums[mid]: left = mid + 1
        
    return -1;


nums = [10,4,3,2,1,-3]
print(find_peak(nums))
            