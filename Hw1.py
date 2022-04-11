# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:10:04 2022

@author: frank
"""
# PPHA 30535
# Spring 2021
# Homework 1

# Franklin Joseph
# fbjoseph123

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
my_list = [5,3,8,7,2,1]
for location, number in enumerate(my_list):
    print ("The value at position", location, "is", number)
##### https://www.geeksforgeeks.org/iterate-over-a-list-in-python/


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.
def isPalindrome(str):
    rev = ''.join(reversed(str))
    if (str == rev):
        return True 
    return False 
str = 'radar'
ans = isPalindrome(str)
if (ans):
    print('Yes')
else: 
    print('No')
str = 'Apple'
ans = isPalindrome(str)
if (ans):
    print('Yes')
else: 
    print('No')
str = "A man, a plan, a canal, Panama!"
ans = isPalindrome(str)
if (ans):
    print('Yes')
else: 
    print('No')
str = "This isn't a palindrome"
if (ans):
    print('Yes')
else: 
    print('No')
########## https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
########## https://www.javatpoint.com/how-to-reverse-a-string-in-python
########## https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
########## https://www.geeksforgeeks.org/python-list-reverse/

# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
split = choice.split()
if split[-1] == 'carrot':
    print ('You can have a carrot')
elif split[-1] == 'kale':
    print ('You can have kale')
elif split[-1] == 'radish':
    print ('You can have radish')
elif split[-1] == 'pepper':
    print ('You can have pepper')
else: 
    input ('You made an invalid choice. Please pick a vegetable I have available: ')
########### https://www.codespeedy.com/get-the-last-word-from-a-string-in-python/
########### https://chercher.tech/python-questions/check-element-list-python#:~:text=In%20python%2C%20the%20in%20operator,%22dog%22%2C%204.8%20%5D.
########### https://www.programiz.com/python-programming/if-elif-else
########### https://www.geeksforgeeks.org/python3-if-if-else-nested-if-if-elif-statements/

# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
old_string_list = ['Cat','Bat','Mat','Asphalt','aArdvark']
conditions = ['A','B','a','b']
new_list = [word.lower() for word in old_string_list if word.startswith(tuple(conditions))]
print(new_list)
########## https://www.delftstack.com/howto/python/python-lowercase-list/#use-the-method-of-list-comprehension-to-convert-a-list-of-strings-to-lowercase-in-python
########## https://riptutorial.com/python/example/767/conditional-list-comprehensions#:~:text=Given%20a%20list%20comprehension%20you,if%20conditions%20to%20filter%20values.&text=For%20each%20in%20%3C,%3E%20)%20to%20the%20returned%20list.
########## https://stackoverflow.com/questions/34775295/python-startswith-for-loop-and-if-statement
########## https://blog.finxter.com/python-string-startswith-how-to-test-multiple-values/#:~:text=any()%20Function-,To%20check%20if%20a%20given%20string%20starts%20with%20any%20of,)%20for%20x%20in%20prefixes)%20.

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]
finished_list = [26 if number == 3 else 22 if number == 5 else 18 if number == 7 else 14 
                 if number == 9 else 10 if number == 11 else 6 if number == 13 
                 else '' for number in start_list]
print(finished_list)
############# https://riptutorial.com/python/example/767/conditional-list-comprehensions#:~:text=Given%20a%20list%20comprehension%20you,if%20conditions%20to%20filter%20values.&text=For%20each%20in%20%3C,%3E%20)%20to%20the%20returned%20list.
############# https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
state_dict = {short_names[x]:long_names[x] for x in range(len(short_names))}
print(state_dict['IN'])
print('State dictionary:',state_dict)
########### https://pythonguides.com/python-creates-a-dictionary-from-two-lists/
