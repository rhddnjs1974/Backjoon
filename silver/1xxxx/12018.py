import sys
input = sys.stdin.readline

n,m = map(int,input().split())

can = []

for i in range(n):
    p,l = map(int,input().split())
    arr = list(map(int, input().split()))
    if l>p:
        can.append(1)
        continue


    arr.sort()
    arr.reverse()
    can.append(arr[l-1])

can.sort()
ans = 0
for i in can:
    if m>=i:
        ans+=1
        m-=i
    else:
        break
print(ans)