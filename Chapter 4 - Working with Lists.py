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

