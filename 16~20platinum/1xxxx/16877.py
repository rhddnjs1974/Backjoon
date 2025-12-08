import sys
input = sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))
fibo = [1,2]
for i in range(32):
    fibo.append(fibo[i]+fibo[i+1])

dp = [0]*(3000001)
for i in range(3000001):
    mexmade = [0]*32
    for j in range(0,32):
        if fibo[j]>i:
            break
        mexmade[dp[i-fibo[j]]] = 1

    for j in range(0,32):
        if mexmade[j]==0:
            dp[i] = j
            break
a=0

for i in range(n):
    a^=dp[arr[i]]

if a==0:
    print("cubelover")
else:
    print("koosaga")