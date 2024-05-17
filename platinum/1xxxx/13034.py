import sys
input = sys.stdin.readline

n = int(input())

a = 0
mex = [0]*(n+1)
mex[2] = 1

for i in range(3,n+1):
    dp = []
    for j in range(i//2):
        dp.append(mex[j]^mex[i-2-j])

    for j in range(n+1):
        if j not in dp:
            mex[i] = j
            break

if mex[n]==0:
    print(2)
else:
    print(1)
