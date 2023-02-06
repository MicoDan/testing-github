import math

#inputs

# name = input('what is your name')
# color = input('what color do you like?')
# print(name + ' likes '+ color)

#program that takes the year that you were born in and returns your age

# year = input('Enter the year that you were born in: ')
# age = 2023 - int(year)
# print(f'your age is: {age}')

#------------
#prints numbers from 0 to 3
# course = 'Python For Beginners'
# print(course[0:3]) # 0>x<3

# course = 'python for beginners'
# print(course.find('p')) #prints the index of p

#powers

# print(2 ** 3)

#modules

# print(math.ceil(2.4))
# print(math.floor (2.4))

# if has_good_credit and not has_criminal_record

#exercise

# weight = input('weight: ')
# measure = input('l(bs) or kg(kilograms')

# if measure.upper() == 'L':
#     calc = int(weight) / 2.2
# elif measure.upper() == 'KG':
#     calc = int(weight)

# i=0
# while i<3:
#     guess =  input(f'GUESS {i} ')
#     while i==3:
#      break  
# if int(guess) > 17:
#        print('A little lower')
# elif int(guess)==17:
#       print('Correct!')
# else:
#     print('A little higher')
#     i += 1

    #alternative 

#     guess_count = 0
# guess_limit = 3
# secret_number = 9

# while guess_count < guess_limit:
#     counting = int(input(f'Guess {guess_count}'))
#     guess_count += 1
#     if counting == secret_number:
#         print('Congratulations!! You won')
#         break
# else:
#     print('sorry you failed')
   

# print(f'your weight is {calc} kilos')

#for the following program you can also do it easier with booleans


input1 = input()
limit = 1
count1 = 1
count2 = 1

while input1.upper() == 'HELP':
    while limit < 2:
     print('start - to start the car')
     print('stop - to stop the car' )
     print('quit - to exit')
     limit += 1
    input2 = input()
    if input2 == 'start':
        if count1 >= 2:
            print('you\'ve already started the car!')
        else:
         print('car started ready to go....')
         count1 += 1
       
    elif input2 == 'stop':
        if count2 >= 2:
            print('the car has already been stopped!')
        else:
         print('car stopped')
         count2 += 1
        
    elif input2 == 'quit':
        break
    else:
        print('i didn\'t understand that')

else:
    print('I didn\'t understand that')
