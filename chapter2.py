#Here are the notes from chapter 2 from the book. 

#This is python code, where you can "print" messages using "" marks and using the print fucntion 
#Here is an example:
print("Hello World")

#Variables 

#Variables are containers that house a value in which they reference. You can assign a value for a variable and call it 
#When you need it. Here is an example: 

message = "Hello Python World!" # "Hello Python World" is the value and "message" is the variable. 

print (message) #To print your variable's value. 

#Make sure that you use good naming conventions when naming your variables. You need to make sure you spell them correcrtly
#Make sure that they do not share the same name as python functions as "print" and using uppercase letters and 
#Make sure that you use ___ and NOT spaces when using longer named variables. And also dont confused with 0 (zero) and 
# o (the letter O) when coding.

#Strings 

"This is a string" #Strings are contained with single or double quotes, python will recognize this as a string with this. 

#Methods 

name = "carlos huerta-enciso" 

print(name.title()) #.title() is a method that makes the first letter of each word capitilized. 
#You can see that in the code, my name is lower-case and now with .title() it is now capitilized. 

#Methods are actions in python where they can act upon a piece of data. 

#Here is another one. 

name = "carlos" 

print(name.upper()) #.upper() helps make THE WORDS IN ALL CAPS. 

print(name.lower()) #.lower() helps make the words in all lower case letters. 

# f-strings 


first_name = "Carlos"

last_name = "Huerta-Enciso" 

full_name = f"{first_name} {last_name}" #f-strings or format strings, instead of printing one variable at a time, you 
#can use brackets for multiple variable names. 
print(full_name) 

#Here is another example: 

console_1 = "Xbox Series X" 

console_2 = "Playstation 5" 

console_3 = "Nintendo Switch 2" 

current_inventory = f" We currently have {console_1} , {console_2} and {console_3} in stock"

print(current_inventory)
#You can also use methods for f-strings. 

#Whitespaces in python are non-printing characters that can help make your output more organized. 

#Here is the tab function

print("\tPython") 

#  Python

#The tab function is basically tab for your output (which pushed it to the side) 

#Here is the newline tab (basically have each output on top of each other. 

print("Consoles: \nXbox \nPS5 \nSwitch2")
#Consoles: 
#Xbox 
#PS5 
#Switch 2 

#Here is an example of newline and tab whitespaces 

print("Consoles: \n\tXbox \n\tPS5 \n\tSwitch 2 ")

#Consoles: 
#  Xbox 
#   PS5 
#   Switch 2 









