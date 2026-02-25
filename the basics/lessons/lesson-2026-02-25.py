#What Are Dictionaries, and How Do They Work?

#This is the general syntax of a Python dictionary:

dictionary = {
    "key1": 1,
    "key2": 2
}

pizza= {
    "name": "peperony",
    "price": 10,
    "toppings": ["cheese","mushroom","peperony"]
}
print(pizza["name"])

#Another alternative would be using the dict() constructor, which builds the dictionary from a sequence of key-value pairs.

pizza2= dict([("name","peperony"),("price",10),("toppings",["cheese","mushroom","peperony"])])
print(pizza2["price"])

#To update a value, you just need to add the assignment operator, followed by the new value.

pizza["name"]= "peperony pizza"

print(pizza["name"])

#The .get() method retrieves the value associated with a key. It's similar to the bracket notation that we just used, but its advantage is that you can set a default value, so you won't get an error if the key doesn't exist:
#dictionary.get(key, default)

print(pizza.get("toppings",[]))

#The .keys() and .values() methods return a view object with all the keys and values in the dictionary, respectively:

print(pizza.keys())
print(pizza.values())
#A view object is just a way to see the content of a dictionary without creating a separate copy of the data.

#The .items() method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values:

print(pizza.items())

#The .clear() method removes all the key-value pairs from the dictionary:

pizza3= {
    "name": "peperony",
    "price": 10,
    "toppings": ["cheese","mushroom","peperony"]
}
print(pizza3.clear())

#The .pop() method removes the key-value pair with the key that you specify as the first argument and returns its value. If the key doesn't exist, it returns the default value that you specify as the second argument. If the key doesn't exist and you don't pass a default value, a KeyError is raised:

pizza4= dict([("name","peperony"),("price",10),("toppings",["cheese","mushroom","peperony"])])
print(pizza4.pop("price",[]))

#In Python 3.7 and more recent versions, the .popitem() method removes the last inserted item:

pizza5= dict([("name","peperony"),("price",10),("toppings",["cheese","mushroom","peperony"])])
print(pizza.popitem())

#And finally, the .update() method updates the key-value pairs with the key-value pairs of another dictionary. If they have keys in common, their values are overwritten.

pizza6= dict([("name","peperony"),("price",10),("toppings",["cheese","mushroom","peperony"])])
pizza6.update({"price":14,"cook time":25})
print(pizza6)


