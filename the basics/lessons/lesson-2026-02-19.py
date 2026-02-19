#What Are Lambda Functions and How Do They Work?

#Here's what the square() function looks like when refactored into a lambda function:

lambda num: num ** 2

#As mentioned earlier, lambda functions are anonymous, so this function no longer has the name square associated with it. Lambda functions are great when you need to use them in higher order functions like this:

numbers= [1,2,3,4]

even_numbers= list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)




