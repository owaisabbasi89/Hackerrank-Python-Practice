'''

You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
S = list(input())

ll = list("")
ul = list("")
d = list("")

for i in S:
    if i.islower():
        ll += i
    elif i.isupper():
        ul += i
    elif i.isdigit():
        d += i
    else:
        continue
        
ll.sort()        
ul.sort()
d.sort()
def ds(lst):
    arr = list(map(int, lst))
    arr.sort(key=lambda x: x%2==0)
    return list(map(str, arr))
        

print("".join(ll),end="")
print("".join(ul),end="")
print("".join(ds(d)),end="")