import sys
input = sys.stdin.readline

n, c =map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
mi = 1
ma = 1000000000
ans = 0
while(mi<=ma):
    mid = (mi+ma)//2
    now = -20000000000
    count = 0
    for i in arr:
        if i>=now+mid:
            count+=1
            now = i
    
    if count<c:
        ma = mid-1
    else:
        ans = max(ans,mid)
        mi = mid+1

print(ans)