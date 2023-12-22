#In Python, a list is a built-in data type used to store a collection of items. Lists are mutable, meaning their elements can be modified after the list is created. They can contain elements of different data types, and the elements are ordered, which means they have a specific position or index in the list.

#an empty list could look like this

Empty_list=[]

#heres how to add another element to the list
lst1=[1,2,3]
new_element=4

lst1=lst1+new_element

#how to access an element at a specidic index in a list

lst2=[1,2,3,4]
element=lst2[2]

#how to print an element in a list using a for loop

lst3=[1,2,3,4]
for element in lst3:
    print (element)

#how to find the length of a list in python

lst4=[1,2,3,4]
length=len (lst4)

#Python program to find the sum of all numbers in a list using a for loop:

lst5=[1,2,3,4]
sum_of_elements=0

for element in lst5:
    sum_of_elements +=element

print(sum_of_elements)

#What is a nested for loop, and how can it be used to work with lists of lists in Python?
#A nested for loop is a loop inside another loop. It can be used to iterate over elements in lists of lists. For example, if you have a list of lists (a 2D list), you can use nested loops to access each element:

lst6=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]

for row in lst6:
    for element in row:
        print(element)