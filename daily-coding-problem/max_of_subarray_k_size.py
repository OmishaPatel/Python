def max_of_subarray_k_size(arr, n, k):
  max= 0
  for i in range(n-k +1):
    max = arr[i]
    for j in range(1, k):
      if arr[i+j] > max:
        max = arr[i+j]
    print(str(max))

max_of_subarray_k_size([1,2,3,4,5], 5, 3)