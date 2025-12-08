import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    r,c = map(int,input().split())
    arr.append([r,c,i+1])

up = []
down = []
right = []
left = []

ans = 0
ansarr=[]

arr.sort()

t=0
for i,j,k in arr:
    t+=1
    if i<t:
        for a in range(t-i):
            down.append((i,k))
            arr[k-1][0]+=1
            ans += 1
    if i>t:
        for a in range(i-t):
            up.append((i,k))
            arr[k - 1][0] -= 1
            ans += 1

down.sort()
down.reverse()
up.sort()

for i,j in down:
    ansarr.append((j,"D"))
for i,j in up:
    ansarr.append((j,"U"))


arr.sort(key=lambda x:(x[1]))
t=0
for i,j,k in arr:
    t+=1
    if j<t:
        for a in range(t-j):
            right.append((j,k))
            ans += 1
    if j>t:
        for a in range(j-t):
            left.append((j,k))
            ans += 1

left.sort()
right.sort()
right.reverse()

for i,j in left:
    ansarr.append((j,"L"))
for i,j in right:
    ansarr.append((j,"R"))

print(ans)
for i in ansarr:
    print(*i)