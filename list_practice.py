#Part 1
# creating string with long series of words
#a = "Dog, Cat, Panda, Koala, Ann, Andy, Bob, Brad, Apple, Banana"
# creating a1 variable which is a ist by spliting variable a at ', '. 
#a1 = a.split(', ')
#print(a1)
['Dog', 'Cat', 'Panda', 'Koala', 'Ann', 'Andy', 'Bob', 'Brad', 'Apple', 'Banana']
# deleting word using pop
#a1.pop(3)
#print(a1)
# pop removes the index of the item specified in the list. As i referenced 3rd index in pop function it removed 'Koala' which is the third element in list
['Dog', 'Cat', 'Panda', 'Ann', 'Andy', 'Bob', 'Brad', 'Apple', 'Banana']
#deleting word using remove
#a1.remove('Andy')
#print(a1)
#below andy is removed from the list
['Dog', 'Cat', 'Panda', 'Koala', 'Ann', 'Bob', 'Brad', 'Apple', 'Banana']
#deleting word using del
#del a1[3:6]
#print(a1)
#below starting at index 3 and ending at 6th index all those words wereremoved
['Dog', 'Cat', 'Panda', 'Bob', 'Brad', 'Apple', 'Banana']
#Sorting the list
#a1.sort()
#print(a1)
['Andy', 'Ann', 'Apple', 'Banana', 'Bob', 'Brad', 'Cat', 'Dog', 'Koala', 'Panda']
# adding word to list using append
#a1.append('Mango')
#print(a1)
['Dog', 'Cat', 'Panda', 'Koala', 'Ann', 'Andy', 'Bob', 'Brad', 'Apple', 'Banana', 'Mango']
# adding word to list using insert
#a1.insert(4,'Lion')
#print(a1)
#inserting lion at the 4th index
['Dog', 'Cat', 'Panda', 'Koala', 'Lion', 'Ann', 'Andy', 'Bob', 'Brad', 'Apple', 'Banana']
# adding word using extend
#a2 = ['Lemon']
#a1.extend(a2)
#print(a1)
#added lemon from the list a2 to list a1 using extend
['Dog', 'Cat', 'Panda', 'Koala', 'Ann', 'Andy', 'Bob', 'Brad', 'Apple', 'Banana', 'Lemon']
#converting list back to string
#b = ', '.join(a1)
#print(b)
#Dog, Cat, Panda, Koala, Ann, Andy, Bob, Brad, Apple, Banana

#Part 2

#Nested Lists
li = [1,[2,3],5,6,7,8]
# In the above list [2,3] is an example of nested list as it is a list within a list

# Example of * operator
li_1 = [1,2,3,4]
#print(li_1 * 3)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# By  using '*' operator i am multiplying the items in the list

#Examples of list slices
a1 = ['Dog', 'Cat', 'Panda', 'Koala', 'Ann', 'Andy', 'Bob', 'Brad', 'Apple', 'Banana']
#print(a1[:4])
['Dog', 'Cat', 'Panda', 'Koala']
# In this example i am slicing the list to print from 0th index to 4th index
print(a1[:-2])
['Dog', 'Cat', 'Panda', 'Koala', 'Ann', 'Andy', 'Bob', 'Brad']
# In this example i am slicing the list to print items minus the last two items

# Example of "+=" operator
li_1 = [1,2,3,4]
li_2 = 5
li_1 += [li_2]
print(li_1)
[1, 2, 3, 4, 5]
#In the above example using += operator to append the li_2 which is a list element into list li_1
def sum_total(li_1):
    #creating temp variable to keep total of nums in list as we go through the loop
    total = 0
    for num in li_1:
        # every time loop runs num gets updated with items from the list and is addded to the variable total
        total += num
    return total
#print(sum_total(li_1))
#15
# In above example using += operator to return sum of all the items in list li_1

# Example of list filter
li_3 = [6, 7, 10, 62, 28, 39]
for num in li_3:
    if num % 2 == 0:
        print(num, end= ' ')
 #6 10 62 28 
#Above is an example of filter as i am filtering through the list to print only the even numbers

#Example of a list operation that is legal but does the "wrong" thing, not what the programmer expects 

li_4 = [1,2,3,4,5,6,7,8,9]
#here it suppose to append 10 to the list but instead returns none. this is because append method does not return anything it only modifies the original list
li_4 = li_4.append(10)
print(li_4)
#Ouput:
#None
li_4.append(10)
print(li_4)
# here 10 is appended to the list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      

