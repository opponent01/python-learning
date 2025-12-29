intger=55
float_1=13.23



print("add:", intger + float_1)
print("subtract:", intger - float_1)
print("multiply:", intger * float_1)
print("divide:", intger / float_1)

print("to the power of:", intger ** float_1 )
print("mod:", intger % float_1)
print("floor:", intger // float_1)

int_to_float=float(intger)
print(type(int_to_float))
float_to_int=int(float_1)
print(type(float_to_int))

print("round:",round(float_1))
print("round:", round(float_1,1))

print("abs:", abs(intger))

print("pow:", pow(12,2,5))

box,leftover=divmod(144,3)
print("box:",box)
print("leftover:", leftover)