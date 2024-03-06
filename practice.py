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
n = int(input())

a = set(list(map(int, input().split())))


N = int(input())
for i in range(N):
    c = input().split()
    
    
    if c[0] == 'remove':
        if int(c[1]) in a:
            a.remove(int(c[1]))
            # print(a)
        else:
            continue
    elif c[0] == 'pop':
        a.pop()
        # print(a)
    else:
        a.discard(int(c[1]))
        # print(a)

    
print(sum(a))