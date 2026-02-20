hn= [1]
for i in range(710):
    hn.append(hn[-1]+i*4+5)

dp = [0]
n = int(input())

if n<1792:
    for i in range(1,n+1):
        dp.append(6)
        for x in hn:
            if x>i:
                break
            dp[i] = min(dp[i],dp[i-x]+1)

    print(dp[n])
else:
    hn1 = [0]*(n+1)
    hn2 = [0]*(n+1)
    for i in range(711):
        if hn[i]<=n:
            hn1[hn[i]] = 1
        for j in range(711):
            t = hn[i]+hn[j]
            if t>n:
                continue
            hn2[t] = 1
    
    if hn1[n]==1:
        print(1)
    elif hn2[n]==1:
        print(2)
    else:
        flag=0
        for i in hn:
            if i>n:
                break
            if hn2[n-i]==1:
                print(3)
                flag=1
                break
        if flag==0:
            print(4)