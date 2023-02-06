# people = ['John', 'Paul', 'Sara', 'Susan']
 
# for person in people:
#  if person=='John':
#   print(f'Current Person: {person}')

# for i in range(len(people)): #i is set default to zero and continues increasing with the help of mosh
#     print(people[i]) 

#modules available by default in python

# import datetime
# from datetime import date 
# from time import time

# today = datetime.date.today()
# times = time()
# print(today)
# print(times)

#or

# from datetime import date
# today = date.today()

class User:
    def __init__(self,name):
        self.name = name
