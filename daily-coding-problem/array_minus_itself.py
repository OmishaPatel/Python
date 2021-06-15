nums = [1,2,3,4,5]
n = len(nums)
product = 1
output = []
for i in range(n):
    product *= nums[i]
    output.append(product)

product = 1
for i in range(n-1, -1, -1):
    output[i] = output[i-1]*product
    product*= nums[i]
output[0] = product

print(output)
