import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    f = input().rstrip()
    a = deque()
    n = int(input())
    x = list(input().split(","))
    x[0] = x[0][1:]
    x[-1] = x[-1][:-2]
    
    if n!=0:
        for i in x:
            a.append(int(i))
    
    flag=0
    r=0
    for i in f:
        if i=="R":
            r+=1
        else:
            if a:
                if r%2==0:
                    a.popleft()
                else:
                    a.pop()
            else:
                print("error")
                flag=1
                break
    if flag==1:
        continue
    
    if r%2==1:
        a.reverse()
    
    if len(a)==0:
        print("[]")
    else:
        print("[",end="")
        for i in range(len(a)):
            if i!=len(a)-1:
                print(a[i],end=",")
            else:
                print(a[i],end="]\n")
        