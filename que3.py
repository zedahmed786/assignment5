import math

a = int(input())
b = int(input())
c = int(input())
if a+b > c and b+c > a and c+a > b:
    s = (a+b+c)/2
    print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
else:
    print('Invalid Triangle')