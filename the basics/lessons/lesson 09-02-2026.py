#methods in lists

#The first method we will look at is the append() method. This is used to add an item to the end of the list. 

numbers= [1,2,3,4,5,6]
numbers.append(7)
print(numbers)
#If you want to add one list at the end of another, you can also use the append() method like this

numbers1= [1,2,3,4,5,6]
numbers2= [7,8,9,0]
numbers1.append(numbers2)
print(numbers1)

#Notice how the entire even_numbers list is nested inside of the numbers list.
#But if you want to add all of the individual numbers from the even_numbers list at the end of the numbers list, then you can use the extend() method.
#The extend() method is similar to the append() method, but with extend() you can add multiple elements from one list to another.

numbers3= [1,2,3,4,5,6]
numbers4= [7,8,9,0]
numbers3.extend(numbers4)
print(numbers3)

#To insert an element at a specific index in a list, you can use the insert() method. This method accepts two arguments: the index where you wish to insert the new item and the item you want to insert.

numbers5= [1,2,3,4,5,6]
numbers5.insert(1,1.5)
print(numbers5)

#If you want to remove an element from a list, you can use the remove() method. The remove() method takes the value of the element to remove as an argument

numbers6= [1,2,3,4,5,6,6,7]
numbers6.remove(6)
print(numbers6)
#It is important to note that this method will only remove the first occurrence of an item. Not all of them:
#To remove an element at a specific index in the list, you can use the pop() method like this:


numbers7= [1,2,3,4]
numbers7.pop(1)
print(numbers7)
#If you don't specify an element for the pop method, then the last element is removed.
numbers8= [1,2,3,4]
numbers8.pop()
print(numbers8)

#If you need to empty the list, then you can use the clear() method like this:

numbers9= [1,2,3,4,5,6]
numbers9.clear()
print(numbers9)

#The next method we will take a look at is the sort() method. This method is used to sort the elements in place. Here is an example of sorting a random list of numbers in place:

numbers10= [10.2,4,6,45]
numbers10.sort()
print(numbers10)

#In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list. For example:

numbers11= [10.2,4,6,45]
numbers11sorted= sorted(numbers11)
print(numbers11)
print(numbers11sorted)

#The next method we will take a look at is the reverse() method. This method, will reverse a list of elements in place like this:

numbers12= [4,3,2,1]
numbers12.reverse()
print(numbers12)

#The last method we will take a look at is the index method. This is used to find the first index where an element can be found in a list. 

numbers13= ["hi","hello","bye","goodbye"]
print(numbers13.index("hello"))
#If the element cannot be found, then Python throws a ValueError

