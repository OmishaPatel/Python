import math
def reverse_integer(x):
        
        if x > 0:
            x= str(x)
            x = x[::-1]
            x = int(x)
        else:
            x = str(-x)
            x = x[::-1]
            x = -1 * int(x)
        if x <= math.pow(2, 31) -1 and x >= math.pow(-2,31):
            return x
        return 0
x = 123
x1 = -123
print(reverse_integer(x))
print(reverse_integer(x1))