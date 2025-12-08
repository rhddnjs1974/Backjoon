import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

d = arr[0]
d_arr = []
for i in range(m):
    if arr2[i]==d:
        d_arr.append(i)

ans = []

for k in range(1,m):
    for start in d_arr:
        flag = 0
        for i in range(n):
            if start>=m or arr2[start]!=arr[i]:
                flag = 1
                break
            start += k
        if flag==0:
            ans.append(k)
            break

if len(ans)==0:
    print(-1)
else:
    print(ans[0]-1,ans[-1]-1)