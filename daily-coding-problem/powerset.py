from itertools import combinations
def print_powerset(str):
    for i in range(len(str) + 1):
        for j in combinations(str, i):
            print(''.join(j))
str=['a','b','c']
print_powerset(str)