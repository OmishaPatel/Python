def array_advance(nums):
    furthest_index = 0
    i = 0
    last_index = len(nums) -1
    while i <= furthest_index and furthest_index < last_index:
        furthest_index = max(furthest_index, nums[i] + i)
        i+= 1
    return furthest_index >= last_index

nums= [3, 3, 1, 0, 2, 0, 1]
print(array_advance(nums))

nums = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(nums))
