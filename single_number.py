nums = [1,2,3,4,3,2,1]
single_num = 0
for i in range(len(nums)):
    single_num ^= nums[i]
print(single_num)