
# function to check if num1 and num2 are divisible
def is_divisible(num1,num2):
    # using modulo operator to check if both numbers are divisbile or not
    if num1 % num2 == 0:
        return True
    else:
        return False

# Another way to concise the above function.
#def is_divisible(num1,num2):
    #return num1%num2 == 0

# function to check if a is a power of b
def is_power(a,b):
    # here checking if a is divisible by b by calling helper function is_divisible
    if is_divisible(a,b):
        # here checking conditional a == b to avoid a/b < b output as a result of recursion
        # otherwise, in case of a = 9, b = 3. First iteration 9%3 == 0 is true, then is_power(9/3,3)
        # second iteration 3%3 == 0 is true, then is_power is (3/3,3)
        # third iteration is 2%3 == 0 is false.  So i am putting this condition to prevent function from erroneously returning false as 9 is a power of 3
        if a == b:
            return True
        elif b == 1: #checking this condition to exit the function if b is 1 as 1 to any power won't make another number, so without this it will recurse infinitely 
            return False
        # both a == b and b == 1 serve as a base case for recursion to exit
        else: 
            return is_power(a/b,b)# using the recursive function to return a/b which is a power of b
        
     # here dont have to use else because if the conditions in the 'if' statement were not satisfied function will return false   
    return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))




        
    
