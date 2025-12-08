import sys
n = int(input())
a= 0
b= n+1
x=1
arr = []
for i in range(1,n+1):
    x *= -1
    if x==-1:
        a+=1
        arr.append(a)
    else:
        b-=1
        arr.append(b)
print(*arr)