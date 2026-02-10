#What Are Tuples and How Do They Work?

#A tuple is a Python data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types like this:

words= ("apple", "bannana",20)

#To access an element from a tuple, you can use bracket notation and the index number:
#If you need to access elements starting from the end of a tuple, then you can use negative indexing. Here is an example of using a negative index to access the second to last element in a tuple:
print(words[1])
print(words[-1])

#Another way to create a tuple is by using the tuple() constructor like this:

fruit= "bannana"
print(tuple(fruit))

#To check if an item is in a tuple, you can use the in keyword like this:

numbers= (1,2,3,4,5,6)
print(2 in numbers)

#You can also unpack items from a tuple just like you did with lists:

names=("jason","mike","ali")
name1,name2,name3=names
print(name1)
print(name2)
print(name3)

#If you need to collect any remaining elements from a tuple, you can use the asterisk (*) operator like this:

names2=("jason","mike","ali")
jason,*rest= names2
print(jason)
print(rest)

#Just like with a list, you can use the slice operator on a tuple to extract a portion of it. Here is an example of extracting the items 'pie' and 'cookies' into a separate tuple:

numbers2=(1,2,3,4,5,6,7,8)
print(numbers2[1:3])

#So when might you use a tuple over a list?
#If you need a dynamic collection of elements where you can add, remove and update elements, then you should use a list. If you know that you are working with a fixed and immutable collection of data, then you should use a tuple.
