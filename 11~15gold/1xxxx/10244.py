import math
g = [[0]*101 for i in range(101)]

for i in range(1,101):
    for j in range(1,101):
        g[i][j] = math.gcd(i,j)

while(True):
    n = int(input())
    if n==0:
        break
    arr =[]
    for i in range(n):
        arr.append(int(input()))
    ans = 0
    for i in range(1,101):
        if i in arr:
            ans+=1
            continue
        flag = 0
        d = []
        for x in arr:

            if x%i!=0:
                d = []
                continue
            b = set()
            b.add(x)
            for j in d:
                t = g[j][x]
                if t==i:
                    flag=1
                    break
                b.add(t)
            if flag==1:
                break
            
            d = list(b)
            
        if flag==1:
            ans+=1
    print(ans)