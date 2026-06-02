# Loops 

#Looping lets you work with all the items on the list without the need to execute each item one at a time. 
#This can be applied to a list with even millions of items!
#Do perform the same action with every item in the list, you can use a "for loop"

#Here is an example code of a list of magicians names and we want to print their names all at the same time. 


magicians = ['alice', 'david','carolina']
for magician in magicians: #Here we defined a for loop, this tells python to pull all the name from the list magicians and then store them into the variable "magician"
  print(magician) #It reads the code as " For every magician in the list of magicians, print the magicians name"

#The loop tells pyhton that you need to pull all the names from the list until there are no more. 
#Once python see that there are no items left in the list, the program simply ends. 

#Its important when choosing a name for your loop, a good name would be a name that represents a single item from the list. 
#Example: 

#for cat in cats:
#for dog in dogs: 
#for item in list_of_items: 

#using singular or plural names can help you tell the difference between a list trying to use a single element from a list or all the items from the entire list.

magicians = ['alice','david','carolina']
for magician in magicians:
  print(magician.title()+", that was a great trick!") #You can write as many lines of code for the for loop. Every line of code under the "for magician in magicians"
  #is cosidered inside the loop.
magicians = ['alice','david','carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")
  
#Indentation is very important for when python sees what is in the loop.
#Here is an example of what happens when a line of coe is not in the loop.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!") #With this line of code, this will only be printed once.

#Indentation errors.
#Python does its best when using indentation, makes it easier for you to read code.
#Using whitespaces for you to write neatly written code.
#but sometimes there are times where you can make what is called "indentation errors"

#Always indent the line after the for statement in a loop. Here is an example:

magicians = ['alice', 'david','carolina']
for magician in magicians:
print(magician)
#Once you run  it, python will be expecting indent block, but if it doesn't find one it will let you know which line is the problem.
# Here is the error when you run it: IndentationError: expected an indented block after 'for' statement on line 9

#Forgetting to add indentations
#Sometimes when you forget to indent code, python will run the code without any errors but will not produce the result.
#This can happen when you are trying to run multiple things in a loop and forget to indent some of them.

#Here is an example of this:

magicians = ['alice','david','carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick," + magician.title() + ".\n")

#As you can see, once we forgot to indent the 2nd print statement. Python ran the code and it only counted the 1st print statement
#In the loop. If python can find at least one indented line, then there is no error unlike the previous example before.
#Notice that the final value (carolina) in magicians gets the 2nd print statement.

#This is what is called a "logic error". The syntax is valid according to python, but the code does not produce the result that we
#want, because the problem happens in its logic.
#All you need to do to avoid this, is to see if you need to indent a line or a group of lines.

#Unnecessary indenting

#Try not to indent in places where you do NOT need to indent. Here's an example:

message = 'please do not indent this, please!'
  print(message) #Why did you do it!!!!

  #Just remember, you need to indent where you want the actions to repeat for each item in a for loop.

#Indenting after the loop

#Indenting code after running the loop, will repeat once, for each item on the list. But this will lead to a logic error. 
#Here's an example: 

magicians = ['alice', 'david','carolina']
for magician in magicians: 
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")

  print("Thank you everyone, that was a great magic show!")

  #Again always determine when you want to indent code so it can be counted inside the loop vs. unindent code that it can be counted outside the loop. 

#Forgetting the colon 

# : tells python thsat this is the start of the loop. 

magicians = ['alice', 'david','carolina']
for magician in magicians #Here I forgot to put the : on purpose. 
  print(magician) #As a result python does not know what the hell I'm doing 

#Try it yourself 

#4-1 

pizza_list = ['pepperoni','cheese','meatlovers']
for pizza in pizza_list:
  print("I like " + pizza.title())

#4-2 
animals = ['shark','whale','pistol shrimp']
for animal in animals:
  print("A " + animal.title() + " would make a great pet." )
  print("A " + animal.title() + " would make a great pet, if you like animals of the ocean." + ".\n")
print("All these animals have in common, is that they are from the ocean.")

#Making Numerical lists 

#In python you can make a list of numbers, especially with less code. 
#You can use the range() function to generate a set of numbers pretty easily. 

for value in range(1,5):
  print(value)

#As you can see, it did not print the number 5 but only up to 4. 
#With range() the first digit where (1,) is, is the starting value. And (,5) is the last value. 
#But with programming we are always in that "off by one" lifestyle. 

#If you want to print with 5, all you need to do is add (1,6)
for value in range(1,6):
  print(value)

#Using range() to make a list of numbers 

#If you want to make a list of numbers, you can use the list() function. 
#When you wrap list() around a call to range(), the output will be a list of numbers. 

numbers = list(range(1,6))
print(numbers)

#You can also skip numbers in your list in a given range. 
even_numbers = list(range(2,11,2))
print(even_numbers)

#Here's how we break it down: 

#In range (2,11,2)
# The (2,)

# ** represents exponents, here is an example on how it would work:

squares = []
for value in range (1,11):
  square = value**2
  squares.append(square)

  print(squares)
  
#Now you can make this more clean and shorter by combining "square = value**2" with "squares.append(square)"

squares = []
for value in range(1,11):
  squares.append(value**2)
  print(squares)

from string import digits
#Simple statistics with a list of Numbers

#In python you can find the minimum, the maximum, and the sum of a list of numbers.

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

#List comprehensions

#List comprehensions are a way for you to generate the same list just in one line of code. This is done by using a for loop and the creation of new elements
#into one line and this appends each new element

squares = [value**2 for value in range(1,11)]
print(squares)

#Consider writing your own list comprehensions, it will be worth it at the end.

#4-3 Counting to twenty.

for numbers in range(1,21):
  print(numbers)

#4-4 One Million

for number in range(1,1000001):
  print(number)

#4-5 Summing a Million

numbers = range(1,1000001)
min(numbers)
