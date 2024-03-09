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




# def print_rangoli(size):
#     # your code goes here
#     ls = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     lrwidth = (size+size-1+size+size-2-3)//2
#     for i in range(size):

#         left = ""

#         for j+1 in range(size):
#             print(ls[size-1])
            
#         right = ""
        
#         for k in range(size):
            
            
#         print("ccc".ljust(lrwidth,'-')+(ls[size-1-i]).center(3, '-')+'eee'.rjust(lrwidth, '-'))

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)






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






import re

dates_list = [
    "Today's date is 08/03/2024.",
    "The event will take place on 15/05/2024.",
    "Please submit your report by 30/04/2024."
]

for i in dates_list:
    pattern = '^{2}[0-9]/{2}[0-9]/{4}[0-9]'
    d = re.search(pattern, i)
    print(d)