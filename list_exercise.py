from operator import add
# Exercise 1: reverse a list
aLsit = [100, 200, 300, 400, 500]
#using for loop
for i in range(len(aLsit)//2):
    aLsit[i],aLsit[len(aLsit)-1 -i] = aLsit[len(aLsit)-1 -i],aLsit[i]
print(aLsit)
#using slicing
aLsit = aLsit[::-1]
print(aLsit)


#Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
#using for loop
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
#using list comprehension
list3 = [list1[i]+list2[i] for i in range(len(list1))]
#using zip function
list3 = [i + j for i,j in zip(list1,list2)]
#using sum and map
list3 = list(map(add, list1, list2 ))
print(list3)


#Exercise 3: Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
aList = [i * i for i in aList]
print(aList)



#Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [i+j for i in list1 for j in list2]
print(list3)


#Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1,list2[::-1]):
    print(i,j)


#Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#using list comprehension
list2 = [i for i in list1 if i]
#using join() and split()
list2 = ' '.join(list1).split()
#using filter
list2 = list(filter(None,list1))
print(list2)


#Exercie 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ['h','i','j']
list1[2][1][2].extend(sublist)
print(list1)

#Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)


# Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 10, 15, 20, 25, 50, 20]
list2 = [i for i in list1 if i!=20]
print(list2)