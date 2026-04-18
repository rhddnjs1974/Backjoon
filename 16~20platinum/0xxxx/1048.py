import sys
input = sys.stdin.readline
# 라이브러리: 누적합.py

def prefix(arr):
    x = len(arr)
    y = len(arr[0])
    s_arr = [[0]*(y+1) for i in range(x+1)]
    for i in range(x):
        for j in range(y):
            s_arr[i+1][j+1] = s_arr[i+1][j] + s_arr[i][j+1] - s_arr[i][j] + arr[i][j]
    return s_arr

def range_sum(parr, startx, starty, lastx, lasty):
    return parr[lastx][lasty] - parr[lastx][starty-1] - parr[startx-1][lasty] + parr[startx-1][starty-1]

MOD = 1000000007
n, m, l = map(int, input().split())
word = input().rstrip()
board = [input().rstrip() for _ in range(n)]
k = len(word)

dp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            dp[i][j] = 1

for step in range(1, k):
    ch = word[step]
    parr = prefix(dp)
    ndp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != ch:
                continue
            total = 0
            if i-2 >= 0 and j-2 >= 0:
                total += range_sum(parr, 1, 1, i-1, j-1)
                total -= dp[i-2][j-2]
            if i-2 >= 0 and j+2 <= m-1:
                total += range_sum(parr, 1, j+3, i-1, m)
                total -= dp[i-2][j+2]
            if i+2 <= n-1 and j-2 >= 0:
                total += range_sum(parr, i+3, 1, n, j-1)
                total -= dp[i+2][j-2]
            if i+2 <= n-1 and j+2 <= m-1:
                total += range_sum(parr, i+3, j+3, n, m)
                total -= dp[i+2][j+2]
            ndp[i][j] = total % MOD
    dp = ndp

ans = 0
for i in range(n):
    for j in range(m):
        ans = (ans+dp[i][j]) % MOD
print(ans)
