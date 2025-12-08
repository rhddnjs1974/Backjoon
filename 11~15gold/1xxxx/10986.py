import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr[0] %= m

for i in range(1,n):
    arr[i] = (arr[i-1]+arr[i])%m

dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

ans = 0
for i in dic:
    t = dic[i]
    ans += t*(t-1)//2

if 0 in dic:
    ans+=dic[0]
print(ans)