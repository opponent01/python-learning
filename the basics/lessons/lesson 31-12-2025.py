#What Are Truthy and Falsy Values, and How Do Boolean Operators and Short-Circuiting Work?
#In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as True or False in a logical context. Many values are considered truthy, that is, they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False.
#use bool() to see if a value is truly or falsy

print(bool(0))
print(bool(""))
print(bool(1))
print(bool("hi"))

#The and operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.


is_citizen=1
age=18

print(is_citizen and age)

if is_citizen and age >=18:
    print("you can vote")
else:
    print("you can not vote")

#Now let's take a look at the or operator. This operator returns the first operand if it is truthy, otherwise, it returns the second operand. An or expression results in a truthy value if at least one operand is truthy. The or operator is also known as a short-circuit operator.

i_have_a_dog=True
i_have_a_cat=True

if i_have_a_dog or i_have_a_cat:
    print("i have pets")
else:
    print("i don't don't pets")

#The last operator we will look at is the not operator which takes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True. Unlike the previous operators we looked at, not always returns True or False.

admin=1

if not admin:
    print("access denied")
else:
    print("access granted")

#How Do Functions Work in Python?
#
#Functions are reusable pieces of code that run when you call them. Many programming languages come with built-in functions that make it easier to get started. Python is no exception, and we've already covered some built-in functions like print() in previous lessons.
#Another helpful built-in function is input(), which lets you prompt the user for input:

# name= input("enter your name")
# print("hello", name)


#You can also write your own custom functions. To do that, you use the def keyword, followed by the name you want to give your function, a pair of parentheses, and a colon. Then on a new line, you write the code your function should run. The code the function runs is also referred to as the function's body.

def hello():
    print("hello there")
hello()

def add(a,b):
    return a + b

print(add(12,24))
