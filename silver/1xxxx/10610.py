import sys
input = sys.stdin.readline

n = input().rstrip()
x = 0
t = 0
for i in n:
    if int(i)==0:
        t=1
    x+=int(i)

if t==0 or x%3!=0:
    print(-1)
else:
    arr = []
    for i in n:
        arr.append(i)
    arr.sort()
    arr.reverse()
    for i in arr:
        print(i,end="")