nums = [1,2,6,4,7]
nums1 = {*nums}
n = len(nums)
#usig hashing with O(n) time and space O(1)
def first_missing_positive(nums):
    index = 1
    while True:
        if index not in nums:
            return index
        index+=1
print(first_missing_positive(nums))
#using sorting algo with time O(n) and Space O(n)
def first_missing_positive1(nums):
    # checking if there is 1 in array or note
    contains_one = False
    for x in nums:
        if x == 1:
            contains_one = True
            break
    if not contains_one: return 1

    n = len(nums)
    if n == 1: 
        return 2
    # converting nonpostive any integer greater than n to 1
    for i in range(n):
        if nums[i] <=0 or nums[i] > n:
            nums[i] = 1
    #converting the positive integer to negative using sorting algorithm
    for i in range(n):
        x = abs(nums[i])
        if nums[x-1] > 0:
            nums[x-1] *= -1
    # getting index where there is positive element
    for i in range (n):
        if nums[i] > 0:
            return i + 1
    return n+ 1
print(first_missing_positive1(nums))
