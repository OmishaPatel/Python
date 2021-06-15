nums = [11,20,3,4,5]
target = 8

def two_sum(nums,target):
    if len(nums) <= 1:
        return False
    aux_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in aux_dict:
            return aux_dict[complement], i
        else:
            aux_dict[nums[i]] = i
            print(aux_dict)
print(two_sum(nums,target))

