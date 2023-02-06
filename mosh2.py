# for item in 'Python':
#     print(item)

# for i in range(4):
#     for j in range(4):
#         if i==0 and (j==0 or j==1 or j==2 or j==3 or j==4):
#             print('*')
#         elif i==1 and (j==0 or j==1):
#             print('*')
#         elif i==2:
#             print('*')
#         elif i==3 and (j==0 or j==1):
#             print('*')
#         elif i==4 and (j==0 or j==1):
#             print('*')
#         else:
#             print(' ')
#     print("\n")

# numbers = [3, 6, 2, 8, 2, 4, 10]
# new=[]


#importance of in and not in

# for number in numbers:
#     if number not in new:
#         new.append(number)

# print(new)

#tuples

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# numbers = (1, 2, 3)
# #numbers[0]

# x, y, z = numbers
# print(x, y, z)
 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
# from googlesearch import search

# query= 'python dictionaries'

# for url in search(query):
#     print(url)

#dictionaries

# ch = input('')

# obj = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }


# for x in ch:
#     print(obj[x])#gets the value of x

# message = input(">")
# words = message.split(' ')

# emojis = {
#     ":)":"😊",
#     ":(":"😞"
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

