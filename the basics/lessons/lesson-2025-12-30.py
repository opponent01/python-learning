#How Do Augmented Assignments Work?
#Augmented assignment combines a binary operation with an assignment in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable.

intger_1=13
intger_1+=5
print("add:",intger_1)

intger_2=13
intger_2-=5
print("subtract:", intger_2)

intger_2+=12
print("add and sub?:", intger_2)

intger_3=13
intger_3*=5
print("multiply:",intger_3)

intger_4=13
intger_4/=5
print("divide:", intger_4)

#also works with the other oprations like floor or mod
#and it works for concatenate srings or repeat them
string_1="hello"
string_1+=" how are you?"
print(string_1)

string_2="hi!"
string_2*=3
print(string_2)

#How Do Conditional Statements and Logical Operators Work?
#Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.

print("equal:", 12==12)
print("not equal:", 12!=12)
print("greater than:", 12>11)
print("lower than:", 12<11)
print("greater or equal:", 12>=12)
print("lower or equal:", 12<=13)

#the if

age=75

if age >=18:
 print("you are an adult")
else:
 print("you are not an adult")

#you can use elif for another if statement if the first condition is flase

if age >=60:
 print("you are old")
elif age >=30:
 print("you are middle aged")
elif age >= 18:
 print("you are an young adult")
elif age >= 13:
 print("you are a teenager")
else:
 print("you are a child")