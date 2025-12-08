import sys
input = sys.stdin.readline

n = int(input())
k = list(map(int,input().split()))

s = sum(k)
arr = k+k
ans= 0

for i in range(n):
    a = 0
    now = 0
    for j in range(n):
        a+=arr[i+j]
        if a<0:
            ans += int(-a//s)
            if -a%s!=0:
                ans+=1

print(ans)