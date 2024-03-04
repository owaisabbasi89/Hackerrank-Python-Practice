a = input("enter: ")
r = s.title()
c = list(r)
d = []

for i in range(len(c)):
    if c[i].isalpha() and c[i-1].isdigit():
        d.append(c[i].lower())
    else:
        d.append(c[i])

print("".join(d))