#How Do Loops Work?

numbers= [1,2,3,4,5,6,7,8]
for number in numbers:
    print(number)

#You can also use a for loop to iterate through other iterables like a string. Here is an example of using a for loop to loop through the string code and print out each character:
for char in "hello":
    print(char)    

#Just like in JavaScript, you can also nest for loops in Python. Here is an example of using a nested for loop:

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

#Another type of loop you can use in Python is the while loop. This type of loop will repeat a block of code until the condition is False. Here is an example of using a while loop for a guessing game:
"""
secret_number= 5
guess= 0 

while guess != secret_number:
    guess= int(input("please enter you guess(1-10)"))
    if guess != secret_number:
        print("wrong try again")
print("good job!")
"""
#Just like in JavaScript, Python supports the break and continue statements.

#The break statement is used to stop the execution of a loop. Here is an example of using the break statement for a list of developer_names:

dev_names= ["amir","ali","arash"]
for devs in dev_names:
    if devs == "arash":
        break
    print(devs)

#The continue statement is used to skip the current iteration of a loop and move onto the next iteration. Let's modify the example from earlier to use the continue statement instead of break:

for devs in dev_names:
    if devs == "ali":
        continue
    print(devs)

#Both for and while loops can be combined with an else clause, which is executed only when the loop is not terminated by a break statement. Here is an example of using multiple for loops:

words = ['sky', 'worlds', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' had no vowels")



