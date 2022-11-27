#1.3.1 Test questions on number

#1, If you divide two integers with the /-operator, is the resultat always an integer (as it is in the programming language C)?
# In c++, if the result is uneven then the programm will round it upward and result in an integer, 
# while python return a uneven number as float, for exampel 5/2 = 2.5 instead of 3

#2. How do you achieve integer division in python?
#answer: by including an extra /, for example 5//2 instead of 5/2

#3. What is 2**-1 ? 
# 0.5 , think 2^-1


#1.3.2 Test questions on Strings

#1. What is 15*"spam " ?
#answer spamspamspamspamspamspamspamspamspamspamspamspamspamspamspam

#2. What is the easiest way to write a multi-line string?
#answer by using multi = '''text1 text2 text3'''

#3. What is the easiest way to write a string that contains citation symbols (quotation marks)?
#answer print("AAA \" \" AAA ")

#4. Assume that s = "Hello, world!"
#(a) What is then s[0:5] ? answer Hello
#(b) What is then s[:5] ? answer  Hello
#(c) What is then s[-1] ? answer ! 

#5. How do you determine the length of a string?
# answer by using len()

#6. Provoke an error that shows that in python strings are immutable!
# ask johannes 


#1.3.3 Test questions on Lists

#1. Assume we do the following

#a = [100,1,2,3,4,5,6,7]
#r = a
#s = a[0:3]
#t = a[:]
#a[0] = 99
#(a) What is then r ? [99, 1, 2, 3, 4, 5, 6, 7]
#(b) What is then s ? fråga johannes men svar [100, 1, 2]
#(c) What is then t ? [100, 1, 2, 3, 4, 5, 6, 7] fråga också
#(d) In the statement x = y, will y be copied or will x and y refer to the same object? x will take the y value meaning it will print 20,20


#2. How to you determine the length of a list?
# list(NameOfTheList)

#3. What is m[1][0] if m = [[1, 2], [3, 4]]?
# Answer 3 fråga johannes 


#1.3.4 Test questions on First steps...

#1. Assume that a och b are two variables. What does the following statement do? a,b = b,a  
# variabel a gets the value of b and b will get the value of a

#2. Write a while-loop that prints all integers between 1 and 9 on the screen!
from re import X
from tkinter import N


i = 1
while(i<=6):
	#print(i)
	i += 1
  
  
#1.4.1 Test questions on the if-statement

#1. What do you think, why does python use elif instead of else if (as in C)?
 #answer The keyword elif is short for 'else if', and is useful to avoid excessive indentation.
 
#1.4.2 for-statement
#1. Assume that animal = ["dog, "cat", "elefant"]. Write a for-statement that prints all elements of animal!
animal = ["dog ", "cat", "elefant"]
for i in animal:
		#print(i)
  
#2. The following code comes from the web-tutorial
#for w in words[:]:
#	if len(w) > 6:
#		words.insert(0, w)
#Why do we loop here over words[:] and not over words ?
#Fråga Johannes 
#answer we are inserting 


#1.4.3 range() function
#1. Use the range()-function to write a for-loop that prints all integers between 0 and 99!

 for x in range(0,100):
  	#print(x)

#2. One might think that the range()-function returns a list, but that is not the case. 
# Use the range- and list-functions to create a list that
#contains all integers between 0 and 99!
  lst = list(range(1,100))
#	print(lst) 


#1.4.4 break, continue, else
#1. A for-loop can have an else-branch. When is that branch executed?
 #fråga johannes
 
 
#1.4.5 Test question empty statement
#1. In a C-program one can see sometimes empty statement in the form
#of a single semicolon or empty curly braces (; or { }). In python one
#uses neither semicolon nor curly braces. How do you write an empty
#statement in python?

## Correct way of writing empty function  in Python
# def fun(): 
 #   pass
 
#1.4.6 Defining functions
#1. Write a function named hello that takes an integer n as input
#parameter and prints the string parrot n times!

def hello( n ):
    #for _ in range(n):
		#print(n *"parrot")

#2. What is f if one writes f = hello?
	f = hello 

#tuples

