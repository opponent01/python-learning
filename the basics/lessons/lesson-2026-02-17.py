#What Are the Enumerate and Zip Functions and How Do They Work?

#In previous lessons you learned how to work with the for loop, which is used to repeat a block of code a set number of times. Here is an example of using a for loop to print each language from the languages list to the console:

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for language in languages:
    print(language)
#But what if you wanted to keep track of the index for each element? Well, one option is to create an index variable and increment it by 1 for each iteration of the loop, like this:

languages2 = ['Spanish', 'English', 'Russian', 'Chinese']
index= 0
for language in languages2:
    print(f"index {index} and language {language}")
    index+= 1

#While that works, an easier way to do that is by using the enumerate() function. The enumerate() function keeps track of the index for an iterable and returns an enumerate object.
#If we pass the languages list to the enumerate() function and convert its returned value into a list with the list() function, it looks like this:


languages3 = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages3)))

#Now, let's refactor the example from earlier to use the enumerate() function:

languages4 = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages4):
    print(f"index {index} and language {language}")

#The enumerate() function also accepts an optional start argument that specifies the starting value for the count. If this argument is omitted, then the count will begin at 0. Here is an example of using the optional start argument:

for index, language in enumerate(languages4, 1):
    print(f"index {index} and language {language}")

#So far we've only been iterating over one list. But what if you need to iterate over multiple iterables in parallel? Well, you can use the zip() function for that, which combines lists into pairs of elements and returns an iterator of tuples.

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

for dev, id in zip(developers, ids):
    print(f"dev: {dev}")
    print(f"id: {id}")



