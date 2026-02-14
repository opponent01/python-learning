#How Do You Work With Integers and Floating Point Numbers?

interger_1=25
interger_2=12

print("addition=" ,interger_1 + interger_2 )
print("subtract=", interger_1 - interger_2)
print("multipy=", interger_1 * interger_2)
print("division=", interger_1 / interger_2)

float_1=33.259
float_2=9.12

print("addition=", float_1 + float_2)
print("subtract=", float_1 - float_2)
print("multiply=", float_1 * float_2)
print("divition=", float_1 / float_2)

#interger+float=float
interger_plus_float= interger_1 + float_1
print(type(interger_plus_float))
print(interger_plus_float)

#The modulo operator (%) returns the remainder when the value on the left is divided by the value on the right

print("modulo=", interger_1 % interger_2)
print("modulo=", float_1 % float_2)
print("modulo=", interger_1 % interger_2 % float_1 % float_2)

#Floor division divides two numbers and returns the greatest integer less than or equal to the result. This is done with the double forward slash operator (//)

print("floor=", interger_1 // interger_2)
print("floor=", float_1 // float_2)
print("floor=", interger_1 // interger_2 // float_1 // float_2)

#Exponentiation raises a number to the power of another, and is done with the double asterisk operator (**)

print("to the power of=", interger_1 ** interger_2)
print("to the poewr of=", float_1 ** float_2)

#Python also provides built-in functions for converting either numeric data or strings into integers or floats.
#The float() function returns a floating-point number constructed from the given number
#The int() function returns an integer constructed from the given number

int_to_float= float(interger_1)
print(type(int_to_float))

float_to_int= int(float_1)
print(type(float_to_int))

#round(): Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer, and returns a whole number with no decimal places:
#also if you put a comma and then a number it will round to that decimal point 
round_this=55.157

print(round(round_this,))

#abs(): returns the absolute value of a number Think of abs() as the "Distance from Zero" tool. It doesn't care about the direction (positive or negative); it only cares about how "far" the number is from the center.

print(abs(interger_1))

#pow(): raises a number to the power of another or performs modular exponentiation.
#Think of pow() as the "Advanced Version" of the exponentiation (**) you just learned. It is a built-in function that can do two things depending on how many numbers you put inside the parentheses.
#If you put two numbers inside, it works exactly like **. pow(base, exponent)
#The "Modular" Way (Power + Leftover)
#This is where pow() becomes a superhero. If you put three numbers inside, it does the power first, then immediately finds the modulo (remainder). pow(base, exponent, modulus)

print(pow(25, 13, 2))

#we have divmod()that does the floor and mod at the same time

print(divmod(157, 5))

#we also can hold multiple variables in one line in order if you put a comma in between

box,leftover= divmod(157,5)
print("box:", box)
print("leftover:", leftover)