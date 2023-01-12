def selectionSort(arr: list[int]) -> None:
    for i in range(len(arr) - 1):
        pivot = arr[i]
        smallest_index = i
        
        for j in range(i, len(arr)):
            if arr[j] < pivot:
                smallest_index = j
                
        print(arr[smallest_index])
        print(arr)
        [arr[i], arr[smallest_index]] = [arr[smallest_index], arr[i]]
            
            
nums = [4, 3, 11, 23, 17, 13, 199, 121, 147, 179]
selectionSort(nums)
print(nums)