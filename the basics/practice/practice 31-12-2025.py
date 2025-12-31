print(bool(0))
print(bool(1))

citizen=1
age=15

if citizen and age >=18:
    print("you can vote")
elif citizen==False:
    print("you are not a citizen")
elif  age <18:
    print("you are underage")

i_have_a_dog=1
i_have_a_cat=1

if i_have_a_dog or i_have_a_cat:
    print("i have pets")
else:
    print("i don't have pets")

admin=0
if not admin:
    print("access denied")
else:
    print("access granted")

name= input("what's your name")
print("hello", name) 

def hello(): 
    print("hello")

hello()

def add(a,b):
    return (a+b)

number= add(1,5)
print(number)
