a = [11,20,3,4,5]
b = 8
c = []
def two_sum(a,b):
    d = {}
    for i in range(len(a)):
        rem = b - a[i]
        print(rem)
        if rem in d:
            return rem, a[i]
        d[a[i]] = a[i]
        print(d)

print(two_sum(a, b))
