def num_ways_climb_stairs(n,x):
  #base case
  if n == 0:
    return 1
  # store value
  result = 0
  for i in x:
    # not counting negative values
    if (n-i >=0):
      result = result + num_ways_climb_stairs(n-i, x)
  return result

x = [1, 3, 5]
n = 5
print(num_ways_climb_stairs(n,x))


def num_ways(n):
  if n < 3:
    return n
  return num_ways(n-1)+num_ways(n-2)


print(num_ways(4))