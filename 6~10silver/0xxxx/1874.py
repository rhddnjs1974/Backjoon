import sys
input = sys.stdin.readline

N = int(input())

arr = []
ans = []
t = 0
flag= 0
for i in range(N):
    x = int(input())
    if t<x:
        while(t<x):
            t+=1
            arr.append(t)
            ans.append("+")
        arr.pop()
        ans.append("-")
    else:
        p = arr.pop()
        ans.append("-")
        if p!=x:
            print("NO")
            flag=1
            break

if flag==0:
    for i in ans:
        print(i)