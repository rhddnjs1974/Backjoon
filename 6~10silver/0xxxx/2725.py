import math
dp = [0,0] #3더하기
for i in range(2,1001):
    x=0
    for j in range(1,i):
        if math.gcd(i,j)==1:
            x+=1
    dp.append(dp[-1]+x)

for i in range(int(input())):
    n = int(input())
    print(dp[n]*2+3)