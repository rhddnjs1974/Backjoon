A = input()
B = input()

n = len(A)
m = len(B)

dp = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        if A[i]==B[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])


ma = 0
for i in dp:
    for j in i:
        ma = max(ma,j)

print(ma)