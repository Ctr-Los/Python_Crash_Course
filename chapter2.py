#Here are the notes from chapter 2 from the book. 

#This is python code, where you can "print" messages using "" marks and using the print function 
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

"This is a string" #Strings are contained with single or double quotes, python will recognize this as a string. 

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



#Whitestrips Methods 

favorite_language = "Python " #Here is an example of whitespaces, where in python does recognize the space in between
#python and " to remove the whitespace you need to use the r.strip() method. 

favorite_language.rstrip() #This will now remove the whitestrip from the right side. 

#Note that using this method is only temporary, as if you run the variable again the whitespace will still appear. 
#In order to remove the whitespace forever, you need to associate the method with the variable like this: 

favorite_language = favorite_language.rstrip()

#Run favorite_language again and you're good to go. 

#Here is how to remove whitespaces from the left. 

favorite_language = " Python" 

favorite_language.lstrip() #Simply use the l.strip() method 

#Now here is the method to do both sides. 

favorite_language = " Python " 

favorite_language.strip()


#Prefix method 

#Python has a method where you can remove the prefix from a string. 
#An example of this, is the https:// on a url link. 
#We want to get rid of that, here's how. 

url_link = "https://bakerripley.org" 

url_link.removeprefix('https://') #And done! If you want to remove this forever, do the same thing as last time and 
#assign the variable with the method. 

url_link = url_link.removeprefix('https://')

#Exercises: 

#2-3 Personal message 

carlos_message = "Hello Carlos, would you like to learn some Python today?"

print(carlos_message)

#2-4 Name cases 

name = "Carlos" 

print(name.upper) #Prints CARLOS 
print(name.lower) #Prints carlos 
print(name.title()) #Prints Carlos 


#2-5 Famous Quotes 

famous_quote = 'Frida Khalo once said: "I paint my own reality and I am my own muse"' 
print(famous_quote) 

#2-6 Famous Quotes 2

famous_person = "Frida Khalo" 

message = "I paint my own reality and I am my own muse" 

famous_message = f"{famous_person} once said: {message}"

#2-7 Stripping names 

name = "\tCarlos" #tab 

name = "\nCarlos" #newline 

name = "Carlos " #Use .rstrip()

name = " Carlos" #Use .lstrip()

name = " Carlos " #Use .strip()

#2-8 File extensions 

filename = "python_notes.txt" 

filename.removesuffix(".txt")

#//////////////

#Numbers 


#Python has numbers but there are different types depending on what you are going to use them for. 

#Integers 

#Integers are basically whole numbers, where in python you can add, subtract, multiply, and divide them. 

2+3 #5

3-2 #1 

2*3 #6 

3/2 #1.5

#using two ** makes an exponent 

3**2 # 9

3**3 #27

10**6 #1000000

#Python also supports order of operations 

2+3*4 #14 

(2+3)*4 #20

#Floats 

#Floats are numbers that have a decimal in them. 

0.1 + 0.1 #0.2 

0.2 + 0.2 #0.4 

2*0.1 #0.2 

2*0.2 #0.4 

#Sometimes you can get strange looking decimal outputs 

0.1 + 0.2 #0.300000000000004 

#Integers and floats 

#Everytime you divide two numbers, you will always get a float as a result. 

4/2 #2.0 

#And when you combine two different types of numbers (ex. a float and a integer) you will also get a float. 
2.0 + 1 #3.0 

2 * 3.0 #6.0 

3.0 ** 2 
9.0 

#Underscores in numbers 

#When you are writing long numbers you can group them using underscores 

universe_age = 14_000_000_000 

print(universe_age) #When you print the variable, python will still keep all the digits together. 

#Multiple assignments 

#You can assign mutiple values to variables on a single line of code. 

x,y,z = 0,0,0 #You need to separate the names with commas as well as the values. 

#Constants 

#Constant is a variable where the value stays the same throughout  the program's life. 
# To do this you need to write the name of the variable in all caps. 

MAX_CONNECTIONS = 50000

#2-9 Number Eight 

print(5+3) #Addition 
print(12-4) #Subtraction
print(4 * 2) #Multiplication 
print(16/2) #Division 

#2-10 Favorite Number 

number = 17 

favorite_number = f"My favorite nunber is:{number} "

print(favorite_number)

#Comments 


#You can make comments using the "#" and python will ignore it. Its basically there for notes. And basically what
#I have been doing this whole time. 

#The Zen of Python 

#The Zen of Python is a set of principals created by Tim Peters, it helps you understand that simple it better than 
#complex. You can access this when you type in "import this" into the interpreter. 

import this 

#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!


#---------------------------------- The end of chapter 2 -------------------------------------------------------------










                              








