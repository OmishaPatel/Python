#Exercise 1: Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
print(aTuple[::-1])

#Exercise 2: Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

#Exercise 3: Create a tuple with single item 50
aTuple = (50),
print(aTuple)

#Exercise 4: Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
a,b,c,d = aTuple
print(a)
print(b)
print(c)
print(d)


#Exercise 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)

#Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)

#Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple2 = sorted(tuple1, key=lambda x: x[1])
print(tuple2)


#Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#Exercise 10: Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
def check_items(tuple1):
    return all(i == tuple1[0] for i in tuple1)
print(check_items(tuple1))
