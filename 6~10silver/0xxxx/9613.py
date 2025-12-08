import math

for i in range(int(input())):
    n,*arr = map(int,input().split())
    
    ans = 0
    
    for x in range(n):
        for y in range(x):
            ans += math.gcd(arr[x],arr[y])
    
    print(ans)