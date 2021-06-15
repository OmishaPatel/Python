def max_non_adjacent_sum(arr):
  last = 0
  before_last = 0    

  N = len(arr)
  for i in range(N):
    # Compute the new 'last'
    new_last = max(
      arr[i],
      arr[i] + before_last,
      last
    )
    
    before_last = last
    last = new_last
    
  return last
print(max_non_adjacent_sum([2,4,6,2,5]))