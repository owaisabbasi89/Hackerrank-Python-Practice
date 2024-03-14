'''
This challenge is only forPython 2.

input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
Task

You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .

Constraints
All coefficients of polynomial  are integers.
 and  are also integers.

Input Format

The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format

Print True if . Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True
Explanation


Hence, the output is True.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
xk = list(map(int, input().split()))
P = input().split()

v = []

for i in P:
    l = list(i)
    aa = ""
    for j in l:
        if j == 'x':
            aa+=str(xk[0])
        else:
            aa+=j
    v.append(aa)

ssd = "".join(v)
if eval(ssd) == xk[1]:
    print('True')
else:
    print('False')