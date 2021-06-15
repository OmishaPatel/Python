def binary_search(arr, target):
    if len(arr) == 1:
        return arr[0]

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return arr[mid]
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
arr = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37
print(binary_search(arr, target))