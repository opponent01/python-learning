#What Are List Comprehensions and What Are Some Useful Functions to Work With Lists?

#For the past few lessons, you have been getting comfortable working with loops like this:

even_numbers= []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

#While this code works, there is a more concise way to write this that uses list comprehension instead. List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets. This makes the code shorter and often easier to read.

even_numbers_2= [num for num in range(21) if num % 2 == 0]
print(even_numbers_2)

#Let's take a look at another example so we can better understand how list comprehension works:

numbers= [1,2,3,4,5,6]
result= [(num, "even")  if num % 2 == 0 else (num, "odd") for num in numbers]
print(result)

#here is the normal version

numbers2= [1,2,3,4,5,6]
for num in numbers2:
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num,"odd")

#The filter() function is used to select elements from an iterable that meet a specific condition. The filter() function accepts a function and an iterable for its arguments.

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words= list(filter(is_long_word, words))
print(long_words)

#Another function to be aware of is the map() function, which takes an iterable and applies a function to each of its elements.

numbers3= [12,23,4,5,67]
def multipy(temp):
    return temp * 2

new_numbers= list(map(multipy, numbers3))
print(new_numbers)

#The last function we will look at is the sum() function. This function is used to get the sum from an iterable like a list or tuple. Here is an example of using the sum() function:

numbers4= [20,10,22,11,4]
the_sum= sum(numbers4)
print(the_sum)

#You can also pass in an optional start argument which sets the initial value for the summation. Here is an updated example using the start argument as a positional argument:

the_sum2= sum(numbers4, 100)
print(the_sum2)





