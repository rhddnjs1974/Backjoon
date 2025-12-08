A = input()
dp = [[] for i in range(26)]
for i in range(52):
    dp[ord(A[i])-65].append(i)

x=0
for i in range(26):
    for j in range(26):
        a,b = dp[i]
        c,d = dp[j]
        if a<c<b and b<d:
            x+=1

print(x)