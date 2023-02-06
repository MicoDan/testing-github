#x=1
#name='john'
#age = 15

#x, y, name, is_cool = (1, 2, 'john', True)

#print ('hello')
#print(x, y, name, is_cool)

#print(type(x))

#x=str(x) #to change the type to a string
#y=int(y)
#y=float(y)

#print(type(y), type(x))
#we concatenate a string only

#print ('hello world '+ str(age))

#print('My age is {age}'.format(age=15))

#print(f'my age is {age}')

#to capitalise letters

#print('hello world'.upper())
#print('hello world'.capitalize())

#print(len('hello world'))

#print('hello world'.replace('world', 'everyone'))

#numbers = [1, 2, 3, 4]

#print(len(numbers))
#Add items to list
#numbers.append(8)
#print(numbers)

#remove items from the list

#numbers.remove(3)
#print (numbers)

#numbers.insert(2, 'strawberries')
#print(numbers)

#sort list =ok
#reverse sort

#numbers.sort(reverse=True) #only works on strings
#print(numbers)

#pop = ok

#dealing with tuples

#fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2=('Apples')
#print (fruits)
#print(fruits2, type(fruits2))

#without the comma the type is regarded as a string but with a comma it is regarded as a tuple

#fruits2 = ('Apples',)
#print(type(fruits2))

#getting values from a tuple is the same as arrays
#!!! TUPLES CAN NOT BE CHANGED

#to delete a tuple

#del fruits2

#set

#fruits_set = {'Apples', 'Oranges', 'Mango'}

#print ('Apples' in fruits_set) # = true 
#to delete a set entirely
#del fruits_set
#to erase only its contents
#fruits_set.clear()
#print(fruits_set)
#to add something to the set = .add()


#DICTIONARIES / like javascript objects

# person = {
#     'first_name':'John',
#     'last_name':'Doe',
#     'age': 30
# }

#another way

#person2 = dict(first_name = 'Sara', last_name='williams')

#print(person, type(person))

#how to access the elements
#print(person['first_name'])

#overriding the age content
#person['age'] = 35 

#adding data 
#person['phone'] = 250
#print(person)

#print(person.keys())
#print(person.items())

#to copy

#person2 = person.copy()
#person2['city'] = 'boston'
#print(person2)

#to remove an item
#del(person['age'])
#or
#person.pop('last_name')
#print(person)

#objects in arrays

# people = [
#     {'name' : 'john', 'aged' : 35},
#     {'name':'martha', 'aged' : 25}
# ]

# print(people[0]['name'])

from googlesearch import search

query = "facebook"

for url in search(query):
    print(url)