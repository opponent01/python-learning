#What Is Scope in Python and How Does It Work?
#In Python, scope determines the point at which you can access a variable. It's what controls the lifetime of a variable and how it is resolved in different parts of the code.
# To correctly determine scope, Python follows the LEGB rule, which stands for the following:
# Local scope (L): Variables defined in functions or classes.
# Enclosing scope (E): Variables defined in enclosing or nested functions.
# Global scope (G): Variables defined at the top level of the module or file.
# Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.

#Local scope means that a variable declared inside a function or class can only be accessed within that function or class.

def func_1():
    var_1="hello"
    print(var_1)

func_1()
#In this case, the my_func function has its own scope which cannot be accessed from outside the function. Calling my_func will output 10, but printing my_var outside the function will lead to a NameError:

#Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.

def func_2():
    msg= "hello there"

    def iner_func():
        print(msg)
    
    iner_func()
func_2()
# However, note that outer functions cannot access variables defined within any nested functions
# That's because res is locally scoped to inner_func. Also, notice that outer_func tries to print res before inner_func is called.
# One solution is to initialize res as an empty string in the enclosing scope, which is within outer_func. Then within inner_func, make res a non-local variable with the nonlocal keyword:


def func_3():
    msg = "how are you?"
    res=""

    def iner_func():
        nonlocal res
        res="i'm fine thank you"
        print(msg)
    iner_func()
    print(res)

func_3()

#Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program. Here, my_var can be accessed anywhere, even inside a function it's not defined in

global_var=21

def func_4():
    print(global_var)

func_4()
print(global_var)

#And if you want to make a locally scoped variable defined inside a function globally accessible, you can use the global keyword:

var_1=20
def show_var():
    global var_2
    var_2=23
    print(var_1)
    print(var_2)
 
show_var()
print(var_2)
 
#You can also use the global keyword to modify a global variable:

var_3=55
def global_var_2():
    global var_3
    var_3=10
    print(var_3)

global_var_2()
#Finally, built-in scope refers to all of Python's built-in functions, modules, and keywords, and are available anywhere in your program

print(str(5))
print(bool(0))
