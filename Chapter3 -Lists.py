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

#Now here's how to remove an element from a list.

#You use the "del" statement

motorcycles = ['honda','yamaha','Suzuki']
del motorcycles[0]
print(motorcycles)

#You can remove an elements from the list at any position.

motorcycles = ['honda','yamaha','Suzuki']
del motorcycles[1]
print(motorcycles) #In both examples you can NO longer access the values after using del statement.

#But if you ever want to keep using a value that you no longer need, you can use the pop() method.
#The pop()method removes the last item from the list BUT let's you work with that item after removing it.
#Here is an example of using pop()

motorcycles = ['honda','yamaha','Suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop() #We pop a value from the list and assigned it to a new variable.
print(motorcycles) #We print the list
print(popped_motorcycles)#We print the pop value to show that we still have access to the value that was removed

 #A greeat use case for the pop() method would be to see what was the last motorcycle we bought.

motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
last_owned = motorcycle.pop()
print(f"The last motorcycle I owned was a : {last_owned.title()} ")

#Popping any positon on a list.
motorcycle = ['honda','yamaha','suzuki']
first_owned = motorcycle.pop(0)
print(f"The First motorcycle I owned was a: {first_owned.title()}")

#If you are ever stuck on using pop() or del statement. Ask yourself this:
#If I want to delete something that I will NEVER use again, I'll go with a del statement.
#If I want to delete something BUT want to use AGAIN, I'll go with with the pop() method.

#In the future, you are going to have hundreds of lines of code and your lists will be as long too.
#Instead of finding an index in a long list, you can add or remove one just by mentioning the value. Here's an example:

motorcycle = ['honda','yamaha','suzuki', 'ducati']
print(motorcycle)

motorcycle.remove('honda')
print(motorcycle) # The remove method, gets rid of the specific element by specifically mentioning by name.


#You can also use the remove method to keep working with an element that was removed

too_expensive = 'ducati' #assign the value to a new variable.
motorcycle.remove('ducati') #We tell python to remove the value from the list
print(motorcycle)
print(f"\nA {too_expensive.title()} is too expensive for me.") #We print the list but are able to use 'ducati' in the new variable too_expensive and make a statement on why we removed 'ducati'
#The remove method deletes the first occurrence of the value we chose but if we need to make all ocurrences are removed we need to create a "loop" (Explained in chapter 7)

#3-4 Guest List

guest_list = ['Brayan', 'Belkis','Jackie','Esme','Jesus','Jesus']
print(f'{guest_list[0]}, you are invited to my event tonight.')
print(f'{guest_list[1]}, you are invited to my event tonight.')
print(f'{guest_list[2]}, you are invited to my event tonight.')
print(f'{guest_list[3]}, you are invited to my event tonight.')
print(f'{guest_list[4]}, you are invited to my event tonight.')
print(f'{guest_list[5]}, you are invited to my event tonight.')

#3-5 Changing Guest List
guest_list = ['Brayan', 'Belkis','Jackie','Esme','Jesus','Jesus']

print(f"Unfortunely {guest_list[2]} will not be able to make it tonight.")

#we will invite denay instead

guest_list.insert(2,'Denay')

print(guest_list)

#3-6 More Guests

guest_list = ['Brayan', 'Belkis','Jackie','Esme','Jesus','Jesus']
print("Good news! We found a bigger table, we can add more people.")
guest_list.insert(0,'Denay')
guest_list.insert(2,'Nora')
guest_list.append('Alej')

print(f'Congrats, {guest_list[0]}. You are invited to my party!!')
print(f'Congrats, {guest_list[1]}. You are invited to my party!!')
print(f"Congrats, {guest_list[2]}. You are invited to my party!!")
print(f'Congrats, {guest_list[3]}. You are invited to my party!!')
print(f'Congrats, {guest_list[4]}. You are invited to my party!!')
print(f'Congrats, {guest_list[5]}. You are invited to my party!!')

#3-7 Shrinking the guest list.


guest_list = ['Brayan', 'Belkis','Jackie','Esme','Jesus','Jesus']
print("Good news! We found a bigger table, we can add more people.")
guest_list.insert(0,'Denay')
guest_list.insert(2,'Nora')
guest_list.append('Alej')

print("Unfortunely I can only invite two people to the event. I am so sorry.")

guest_list.pop(0)
guest_list.pop(1)
guest_list.pop(4)

print(guest_list) # I had to double check who was left on the list.
guest_list.pop(0)
guest_list.pop(2)
print(f'{guest_list[1]}, you are invited to my party!')
print(f'{guest_list[0]} you are invited to my party!')
del guest_list[0]
del guest_list[0]
print(guest_list) #Now its an empty list. 

#Here is how to organize a list using the sort() method.


cars = ['bmw','audi','subaru','toyota']
cars.sort()
print(cars) #Here the list is organized alphabetically, but also using .sort() will change it permanently. Which means we can never revert to the original order as before.

#Now you can to the same but in reverse (backwards), using the reverse=True argument.


cars = ['bmw','audi','subaru','toyota']
cars.sort(reverse=True)
print(cars) # Now its backwards. But also permanent

#If you are wondering how can we still sort the list BUT keep it the same way we had it before, you can use the sorted() method.
#The sorted() method

cars = ['bmw','audi','subaru','toyota']
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars)) #New sorted list using sorted()
print('\nHere is the original list again:')
print(cars) #Printing again the list but will show the original.
#sorted() does also accept reverse=True agrument.
#NOTE that sorting a list alphabetically can be tough when not all values are not all lowercase.

#To reverse the order of the original list, you can use the reverse() method

cars = ['bmw','audi','subaru','toyota']
print(cars)
cars.reverse()
print(cars) #Note that this also makes it permanent, but you can run reverse() again to the same list.

#If you want to find the length of a list you can use the len() method

cars = ['bmw','audi','toyota','subaru']
len(cars) # length is 4 

#3-8 Seeing the world.

favorite_places = ['Japan','Mexico','Germany','Sweden','France']


print(favorite_places)
sorted(favorite_places)

favorite_places = ['Japan','Mexico','Germany','Sweden','France']


favorite_places.reverse()
print(favorite_places)
favorite_places.reverse()
print(favorite_places)

favorite_places = ['Japan','Mexico','Germany','Sweden','France']
favorite_places.sort()
print(favorite_places) #Alphabetized
favorite_places.sort(reverse=True)
print(favorite_places) #Reversed

#3-9 Dinner Guest
guest_list = ['Brayan', 'Belkis','Jackie','Esme','Jesus','Jesus']
len(guest_list)#6


#3-9 Guest list pt.2

guest_list = ['Brayan', 'Belkis','Jackie','Esme','Jesus','Jesus']
print("Good news! We found a bigger table, we can add more people.")
guest_list.insert(0,'Denay')
guest_list.insert(2,'Nora')
guest_list.append('Alej')

len(guest_list) #9

# 3-10 Every Function

twenty_twenty_six_list = ['Read 7 Books','Earn 2 Certifications','Build an app','Become an AI engineer']

print(twenty_twenty_six_list)

#Accessing indexes
print(twenty_twenty_six_list[0])

#Inserting a value in the list

twenty_twenty_six_list.insert(0,'Learn Spanish')
print(twenty_twenty_six_list)

# Using the del statement

del twenty_twenty_six_list[0]
print(twenty_twenty_six_list)

#Using the pop() method


twenty_twenty_six_list.pop(4)
print(twenty_twenty_six_list)

#remove() method

twenty_twenty_six_list.remove('Earn 2 Certifications')
print(twenty_twenty_six_list)
