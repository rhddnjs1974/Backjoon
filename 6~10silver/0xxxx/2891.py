import sys
input = sys.stdin.readline

n,s,r = map(int,input().split())

broke2 = list(map(int,input().split()))
more2 = list(map(int,input().split()))

broke =[]
more = []

for i in broke2:
    if i not in more2:
        broke.append(i)
for i in more2:
    if i not in broke2:
        more.append(i)
broke.sort()
more.sort()
use = []
ans = 0
for i in range(1,n+1):
    if i not in broke:
        ans+=1
        continue

    if i-1 not in use and i-1 in more:
        use.append(i-1)
        ans+=1
        continue

    if i+1 not in use and i+1 in more:
        use.append(i+1)
        ans+=1



print(n-ans)