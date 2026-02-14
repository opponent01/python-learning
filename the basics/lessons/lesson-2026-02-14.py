#What Are Ranges and How Can You Use Them in a Loop?

#The range() function is used to generate a sequence of integers. Here is the basic syntax for the range() function:
#range(start, stop, step)

for num in range(5):
    print(num)
for num in range(1,5):
    print(num)
for num in range(1,10,2):
    print(num)

#If you want to generate a sequence of integers in decrementing order, then you can use a negative integer for the step argument, like this:

for num in range(100,0,-10):
    print(num)

#Another thing you can do with the range() function is create a list of integers by using it with the list constructor. The list constructor is used to convert an iterable into a list

even_numbers= list(range(2,11,2))
print(even_numbers)




