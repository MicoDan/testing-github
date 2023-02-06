#prevent our progtam from crashing once an error is encountered

# try:
#     age = int(input('Age: '))
#     print(age)
#     income = 2000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('age can not be zero')
# except ValueError:
#     print('Invalid value')

# class Point:
#     #constructor to create an object
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         #constructor
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')

# point1 = Point(10, 20)
# point1.x

# class Person:
  
#     def talk(self):
#         print(f'Hi {self.name}')
#     def __init__(self, name):
#         self.name = name

# dan = Person('dan')
# dan.talk()

# class Mammal:
#     def walk(self):
#         print('walk')
        
# class Dog(Mammal):
#     pass

# class Cat(Mammal):
#     pass

# dog = Dog()
# dog.walk()

#to import a module

# import file without extension
# to access an element file.component
#when you import
#import component from ext file 
#then you call it normally

#using modules

# from utils import find_max

# max = find_max([3, 5, 2, 8, 6])

# print(max)

#import from different directory

#ecommerce.shipping = folder.file you can also extend further to import different thing s from another file


#different python modules

#randomness


import random

# for i in range(3):
#     print(random.randint(10, 20))

# members = ['john', 'mary', 'bob', 'mosh']

# leader = random.choice(members)
# print(leader)

# class Dice:
#     def roll(self):
#         print(random.randint(1, 6))
        

# lesson = Dice()
# lesson.roll()

from pathlib import Path

path = Path()


#all files that end with py

#using in place of for each
for me in path.glob('*.py'):
    print(me)

import openpyxl


# from googlesearch import search

# query = "facebook"

# for url in search(query):
#     print(url)