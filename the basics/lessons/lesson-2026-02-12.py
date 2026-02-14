#What Are Some Common Methods for Tuples?

#The first method we will cover is count(). This method is used to determine how many times an item appears in a tuple

number= (1,2,3,4,5,6,2,7,8,9)
print(number.count(2))

#The next method we will look at is the index() method. This method is used to find the index where a particular item is present in a tuple.

number1= (1,2,3,4,5,6,7,8)
print(number1.index(4))

#Another thing you can do with the index() method is to pass in optional start and stop index arguments. Here is an example of passing in an optional start index:

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5
#In this example, we are specifying where to start searching for the string Python. By passing in the number 3 as the second argument to the index() function, we are specifying to start searching at index 3. Since Python appears twice in the tuple, the index() function will return index 5 instead of index 2 because of the use of the optional start index argument.

#You can also pass in an optional stop index. Here is a modified example of specifying a start and stop index:

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2
#Now the result is index 2 because we are starting the search at index 2, and searching up to, but not including, index 5.

alphabet=("a","b","g","c","g","d")
print(alphabet.index("g",3))

#Another commonly used function used with tuples is the sorted() function. In a previous lesson you learned about the sort() method for lists. Well, the sorted() function can be used on any iterable including tuples.

number2= (2,4,6,7,4,5,6,7,8,6,4,31,4,5,2,1)
print(sorted(number2))

#If you need to customize the sorting behavior for an iterable, you can use the optional reverse and key arguments. Here is an example of using key argument to sort items in a tuple by length:

programming_languages2= ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(sorted(programming_languages2, key=len))

#If you want to create a new list of values in reverse order, then you can use the reverse argument like this:

programming_languages3= ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(sorted(programming_languages3))
print(sorted(programming_languages3, reverse=True))
