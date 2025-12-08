import sys
input = sys.stdin.readline
from collections import deque

A = input()
B = input()

dic = {}
for i in A:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] =1
flag = 0

for i in B:
    if i not in dic:
        flag=1
        break
    else:
        dic[i] -=1

for i in dic:
    if dic[i]!=0:
        flag = 1
        break

if flag==1:
    print(-1)
else:
    a = deque()
    b = deque()
    for i in A:
        a.append(i)
    for i in B:
        b.append(i)
        
    idx = 0
    ans = 0
    while(idx<len(A)):
        t = b.pop()
        
        while(idx<len(A)):
            x = a.pop()
            idx+=1
            if x==t:
                break
            else:
                ans+=1
                a.appendleft(x)

    print(ans)