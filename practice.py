# a = input("enter: ")
# r = s.title()
# c = list(r)
# d = []

# for i in range(len(c)):
#     if c[i].isalpha() and c[i-1].isdigit():
#         d.append(c[i].lower())
#     else:
#         d.append(c[i])

# print("".join(d))

# s = input().split()
# print(s)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())

# a = set(list(map(int, input().split())))


# N = int(input())
# for i in range(N):
#     c = input().split()
    
    
#     if c[0] == 'remove':
#         if int(c[1]) in a:
#             a.remove(int(c[1]))
#             # print(a)
#         else:
#             continue
#     elif c[0] == 'pop':
#         a.pop()
#         # print(a)
#     else:
#         a.discard(int(c[1]))
#         # print(a)

    
# print(sum(a))









# #Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))





# Enter your code here. Read input from STDIN. Print output to STDOUT
# N = int(input())
# l = input().split()


# if all(i>0 for i in lint):
#     if any(j<10 for j in lint):
#         print('True')
#     elif any(list(j)==(list(j)[::-1]) for j in l):
#         print('True')
# else:
#     print('False')


# a = '545'
# print(a == a[::-1])


import re

# Given string
text = "I like apples and oranges."

# Regular expression pattern
pattern = r"apple"

# Search for the pattern
if re.search(pattern, text):
    print("The word 'apple' is present.")
else:
    print("The word 'apple' is not present.")
