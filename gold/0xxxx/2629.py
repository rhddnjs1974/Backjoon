import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

m = int(input())
find = list(map(int,input().split()))

dp = [0]*40001
dp[0] = 1
for i in arr:
    for j in range(40000,0,-1):
        if j-i>=0:
            if dp[j-i]==1:
                dp[j] = 1
arr.reverse()

for i in arr:
    for j in range(40001):
        if j+i<40001:
            if dp[j+i]==1:
                dp[j] = 1

for i in find:
    if dp[i]==1:
        print("Y",end=" ")
    else:
        print("N",end=" ")