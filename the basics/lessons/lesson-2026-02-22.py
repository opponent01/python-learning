#Build a Number Pattern Generator

def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    pattern_list= []
    for pattern in range(1,n+1):
        pattern_list.append(str(pattern))
    return " ".join(pattern_list)

print(number_pattern(4))




