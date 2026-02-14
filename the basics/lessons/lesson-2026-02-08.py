#Working with Loops and Sequences

words= ["hi", "hello", "why", "how", "apple"]
print(words[0])

#Another way to create a list is to use the list() constructor. The list() constructor is used to convert an iterable into a list like this:

name= "morgan"
print(list(name))

#To get the total number of elements in a list, you can use the len() function like this:

print(len(words))

#If you wanted to update a value at a particular index, you can do something like this:

list= ["hi", "hello", "why", "how", "apple"]
list[1]= "bye"
print(list)

#If you want to remove an element from a list you can use the del keyword like this:

list2= ["hi", "hello", "why", "how", "apple"]
del list2[0]
print(list2)

#Sometimes it is helpful to check if an element is inside the list. To do that, you can use the in keyword like this:

list3= ["hi", "hello", "why", "how", "apple"]
print("hi" in list3)
print("bye" in list3)

#Sometimes it is common to have lists nested inside of other lists like this:

list4= ["hi", "hello", ["why", "how", "apple"]]
print(list4)

#To access the nested list, you will need to access it using index 2 since lists are zero based indexed:
#Then to access the second language from that nested list, you will need to access it using index 1 like this:

list5= ["hi", "hello", ["why", "how", "apple"]]
print(list5[2])
print(list5[2][1])

#Unpacking values from a list is a technique used to assign values from a list to new variables.

developer= ["alice", 25, "python dev"]
name, age, job= developer
print(name)
print(age)
print(job)

#If you need to collect any remaining elements from a list, you can use the asterisk (*) operator like this:

developer2= ["alice", 25, "python dev"]
name2, *rest= developer2

print(name2)
print(rest)

#The last concept we will look at is the slice operator (:). Similar to strings, you can access portions of a list by using the slice operator like this:

number= [1,2,3,4,5,6,7,8,9,0]
print(number[0:2])

#Another thing you can do with the slice operator : is specify a step interval which determines how much to increment between the indices

number2= [1,2,3,4,5,6,7,8,9,0]
print(number2[::2])

