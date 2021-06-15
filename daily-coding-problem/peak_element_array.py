def find_peak_element(arr):
    l = 0
    r = len(arr) -1

    while (l < r-1):
        mid =(l+r) //2
        if arr[mid] < arr[mid -1]:
            r = mid - 1
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        else:
            l = mid + 1
    if arr[l] >= arr[r]:
        return l
    return r

arr = [1,2,1,3,5,6,4]
find_peak_element(arr)

def find_peak_element_2d(nums):
    n = len(nums)
    m = len(nums[0])

    j = m//2

    row = [i[j] for i in nums]
 
    i = row.index(max(row))

    print(i,j)

    if nums[i][j] < nums[i][j-1]:
        return find_peak_element_2d([row[:j]for row in nums])
    elif j < m - 1 and nums[i][j] < nums[i][j+1]:
        return find_peak_element_2d([row[j:] for row in nums])
    else:
        return nums[i][j]


nums = [ [ 10, 8, 10, 10 ],
        [ 14, 13, 12, 11 ],
        [ 15, 9, 11, 21 ],
        [ 16, 17, 19, 20 ] ]

print(find_peak_element_2d(nums))
# time complexity(O(nlogn))