import sys
input = sys.stdin.readline

n = int(input())

arr=[]

for i in range(n):
    a,b = map(int,input().split())
    arr.append((b,a))

arr.sort()

last = 0
ans = 0
for end,start in arr:
    if start>=last:
        last = end
        ans+=1

print(ans)