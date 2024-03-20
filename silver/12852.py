import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################
dp = [1e9]*3000001
dp[1] = 0
for i in range(1,1000001):
    dp[i+1] = min(dp[i+1],1+dp[i])
    dp[i*2] = min(dp[i*2],1+dp[i])
    dp[i*3] = min(dp[i*3],1+dp[i])

n = int(input())
print(dp[n])

while(n!=1):
    print(n,end=" ")
    if dp[n-1] == dp[n]-1:
        n=n-1
    elif n%2==0 and dp[n//2]==dp[n]-1:
        n = n//2
    elif n%3==0 and dp[n//3]==dp[n]-1:
        n = n//3
print(1)