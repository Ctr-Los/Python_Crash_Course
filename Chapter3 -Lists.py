#Chapter 3 Lists 

#A list can have more than one element in it. In python lists are recognized with square brackets []
# You can use words, digits, and names. And each element is separated by a comma , 
# Here is an example: 


bicycles = ['trek','cannondale', 'redline', 'specialized',]

print(bicycles) 


#When you call the list name, your list will appear with brackets. Here is how to remove them. 

#Python allows you to call a specific element from your list by mentioning the position or "index" 
#Where it is at. Just call the name of the list and wrap the index with a []

bicycles = ['trek','cannondale', 'redline', 'specialized',]

print(bicycles[0])
# You can also use the .title() method to make the output of the element more presentable. 

#In Python, it considers 0 as the first position. In programming languages you can see some unexpected results 
#Therefore you must think that to get any element from a list you must subtract one from its position in the 
#list. 

bicycles = ['trek','cannondale', 'redline', 'specialized',]
print(bicycles[1])
print(bicycles[3]) #Here I printed the 2nd and the 4th elements from the list. 

#Side note: when you ask for an item at -1 index you will get the last item on the list. 
# If you want the 2nd to last item on the list you can use -2 and so forth. 

#You can use f-string for your list, here is an example. 

bicycles = ['trek','cannondale', 'redline', 'specialized',]

message = f"My first bicycle was a {bicycles[0].title()}"
print(message) #My first bicycle was a Trek


#3-1 Names 

names = ['Brayan', 'Belkis', 'Esme', 'Jesus', 'Denay', 'Jesus', 'Emely', 'Nora', 'Alej', 'Jackie' ]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5]) 
print(names[6])
print(names[7])
print(names[8])
print(names[9]) 


#3-2 Greetings


names = ['Brayan', 'Belkis', 'Esme', 'Jesus', 'Denay', 'Jesus', 'Emely', 'Nora', 'Alej', 'Jackie']

message = ',You are welcomed to my birthday party'

print(names[0],message)
print(names[1],message)
print(names[2], message)
print(names[3],message)
print(names[4],message)
print(names[5],message)
print(names[6],message)
print(names[7],message)
print(names[8],message)
print(names[9],message)

#3-3 Your own list


transportation = ['Scout Explorer', 'Electic Bike','Toyota 4Runner','F150']

message = 'I would like to own a:'

print(message,transportation[0])
print(message, transportation[1])
print(message,transportation[2])
print(message,transportation[3])

#We can change the items of a list by just choosing the desired index and assign it with something else.

motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'      
motorcycles[0] = 'ducati'

motorcycles[0] = 'ducati'

print(motorcycles)

#If you want to add a new element to the list, you can use the .append method

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')

#If you want to add a new element to the list, you can use the .append method

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')

print(motorcycles) #appending will add the new element to the end of the list without affecting the other elements on the list.
#You can even append with an empty list.

#Now if you want to add an element to any position on the list, you can use the insert() method.

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
