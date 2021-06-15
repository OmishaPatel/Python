nums = [7,1,5,3,6,4]
#brute force
def buy_and_sell_stock(nums):
    max_profit = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] -nums[i] > max_profit:
                max_profit = nums[j] -nums[i]
    return max_profit

def buy_sell_stock(nums):
    min_value = nums[0]
    max_value = 0
    for num in nums:
        min_value = min(min_value, num)
        compare_profit = num - min_value
        max_value = max(max_value, compare_profit)
    return max_value
print(buy_sell_stock(nums))
print(buy_and_sell_stock(nums))