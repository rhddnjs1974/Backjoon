n = int(input())

nowsum = 0
dp = []
for i in range(36):
    dp.append([0,i])

for _ in range(n):
    x = input()
    x = x[::-1]
    k = 1
    for i in x:
        if i.isdigit():
            nowsum += k*int(i)
            dp[int(i)][0] += (35-int(i))*k
        else:
            nowsum += k*(ord(i)-55)
            dp[ord(i)-55][0] += (35-(ord(i)-55))*k
        k*=36
        
dp.sort(reverse=True)
K = int(input())

for i in range(K):
    nowsum+=dp[i][0]

ans = ""

while(nowsum>0):
    x = nowsum%36
    nowsum //= 36
    if x<10:
        ans+= str(x)
    else:
        ans+= chr(x+55)

ans = ans[::-1]
if ans=="":
    print(0)
else:
    print(ans)