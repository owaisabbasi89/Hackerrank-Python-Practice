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









# import re

# # Given string
# text = "I like apples and oranges."

# # Regular expression pattern
# pattern = r"apple"

# # Search for the pattern
# if re.search(pattern, text):
#     print("The word 'apple' is present.")
# else:
#     print("The word 'apple' is not present.")









# import re

# # Given string
# text = "Hello world"

# # Regular expression pattern
# pattern = '^Hello.*world$'

# # Search for the pattern
# if re.search(pattern, text):
#     print("The string starts with 'Hello' and ends with 'world'.")
# else:
#     print("The string does not start with 'Hello' or does not end with 'world'.")









# import re

# # Given string
# text = "example@email.com"

# # Regular expression pattern
# pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# # Search for the pattern
# if re.match(pattern, text):
#     print("This is a valid email address.")
# else:
#     print("This is not a valid email address.")






# import re

# dates_list = [
#     "Today's date is 08/03/2024.",
#     "The event will take place on 15/05/2024.",
#     "Please submit your report by 30/04/2024."
# ]

# for i in dates_list:
#     pattern = '^{2}[0-9]/{2}[0-9]/{4}[0-9]'
#     d = re.search(pattern, i)
#     print(d)














# array mathematics

# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy as np

# nm = list(map(int, input().split()))

# Aa = []
# for i in range(nm[0]):
#     A = list(map(int, input().split()))
#     Aa.append(A)
    
# Bb = []
# for i in range(nm[0]):
#     B = list(map(int, input().split()))
#     Bb.append(B)
  
# print(np.array(Bb[0]))
# for i in range(nm[0]):
#     print(np.add(np.reshape(np.array(Aa[i]), (nm[0], nm[1])) , np.reshape(np.array(Bb[i]), (nm[0], nm[1]))))
#     print(np.subtract(np.reshape(np.array(Aa[i]), (nm[0], nm[1])) , np.reshape(np.array(Bb[i]), (nm[0], nm[1]))))
#     print(np.multiply(np.reshape(np.array(Aa[i]), (nm[0], nm[1])) , np.reshape(np.array(Bb[i]), (nm[0], nm[1]))))
#     print(np.floor_divide(np.reshape(np.array(Aa[i]), (nm[0], nm[1])) , np.reshape(np.array(Bb[i]), (nm[0], nm[1]))))
#     print(np.mod(np.reshape(np.array(Aa[i]), (nm[0], nm[1])) , np.reshape(np.array(Bb[i]), (nm[0], nm[1]))))
#     print(np.power(np.reshape(np.array(Aa[i]), (nm[0], nm[1])) , np.reshape(np.array(Bb[i]), (nm[0], nm[1]))))


# for i in range(2):
#     print(np.add(np.reshape(np.array(Aa[:nm[1]]), (nm[0], nm[1])) , np.reshape(np.array(Bb[:nm[1]]), (nm[0], nm[1]))))
#     print(np.subtract(np.reshape(np.array(Aa[:nm[1]]), (nm[0], nm[1])) , np.reshape(np.array(Bb[:nm[1]]), (nm[0], nm[1]))))
#     print(np.multiply(np.reshape(np.array(Aa[:nm[1]]), (nm[0], nm[1])) , np.reshape(np.array(Bb[:nm[1]]), (nm[0], nm[1]))))
#     print(np.floor_divide(np.reshape(np.array(Aa[:nm[1]]), (nm[0], nm[1])) , np.reshape(np.array(Bb[:nm[1]]), (nm[0], nm[1]))))
#     print(np.mod(np.reshape(np.array(Aa[:nm[1]]), (nm[0], nm[1])) , np.reshape(np.array(Bb[:nm[1]]), (nm[0], nm[1]))))
#     print(np.power(np.reshape(np.array(Aa[:nm[1]]), (nm[0], nm[1])) , np.reshape(np.array(Bb[:nm[1]]), (nm[0], nm[1]))))













# size = 5
# ls = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# left = ""

# x = 0
# for j in range(len(ls[size])):
#     x += 1
#     # print(j)
#     print(ls[size-1-j:size-1])

# # print(ls[size-1-x:size-1])

# d = 5
# e = 2
# print(e**d)






# def minion_game(string):
#     # your code goes here
#     # if string is "BANANA"
#     lngth = len(string)
#     lst = list(string)
#     cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
#     vow = ['A','E','I','O','U']
#     St = []
#     for i in range(lngth):
#         for j in range(i, lngth):
            
#             x = ''.join(lst[i:j+1])
#             if x[0] in cons:
#                 St.append(x)
#             else:
#                 continue

#     Kv = []
#     for i in range(lngth):
#         for j in range(i, lngth):
            
#             x = ''.join(lst[i:j+1])
#             if x[0] in vow:
#                 Kv.append(x)
#             else:
#                 continue
    
#     if len(St) > len(Kv):
#         print(f"Stuart {len(St)}")
#     elif len(St) < len(Kv):
#         print(f"Kevin {len(Kv)}")
#     else:
#         print("Draw")
            
    

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)










# Enter your code here. Read input from STDIN. Print output to STDOUT

# from itertools import combinations

# KM = list(map(int, input().split()))
# K = KM[0]
# M = KM[1]

# def solver(m, lst):
#     xx = 0
#     for i in lst:
#         xx += i**2
#     return xx%m

# scheme = []
# for i in range(K):
#     scheme.append(list(map(int, (input().split())[1:])))

    

# print(solver(1000, [5, 9, 10]))

# # print(scheme)















# def print_rangoli(size):

#     # your code goes here
#     ls = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     lrwidth = (size+size-1+size+size-2-3)//2
#     for i in range(size):

#         left = ""

#         for j in ls[size-i:size]:
#             left += f"-{j}"
            
#         right = ""
        
#         for k in ls[size-i:size]:
#             right += f"{k}-"
            
            
#         print(left.rjust(lrwidth,'-')+(ls[size-1-i]).center(3, '-')+right.ljust(lrwidth, '-'))



# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


for i in range(1,int(input())+1):
    print((sum(map(lambda x: 10**x, range(i))))**2)

