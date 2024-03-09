import sys
input = sys.stdin.readline

S = input()
q = int(input())
dp = [[0]*26 for i in range(200002)]

for i in range(1,len(S)+1):
    x = ord(S[i-1])-97
    for j in range(26):
        if x==j:
            dp[i][j] = dp[i-1][j]+1
        else:
            dp[i][j] = dp[i-1][j]



for i in range(q):
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    x = ord(a)-97
    print(dp[r+1][x]-dp[l][x])