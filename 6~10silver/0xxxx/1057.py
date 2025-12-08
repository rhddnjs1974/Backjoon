import sys
input = sys.stdin.readline

N,A,B = map(int,input().split())

A,B = min(A,B),max(A,B)

a = []
for i in range(1,N+1):
    if i==A or i==B:
        a.append(1)
    else:
        a.append(0)

flag=0
round=0
while(flag==0):
    round+=1
    stack = []
    x=0
    while(x<len(a)):
        if x+1==len(a):
            stack.append(a[x])
            break
        if a[x]==1 and a[x+1]==1:
            print(round)
            flag=1
            break
        if a[x]==1 or a[x+1]==1 :
            stack.append(1)
        else:
            stack.append(0)
        x+=2
        
    a = stack[:]
