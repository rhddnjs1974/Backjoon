import math
arr= list(map(int,input().split()))

ans = 0
for i in range(len(arr)):
    if math.gcd(i+1,arr[i])>1:
        ans+=1

print(ans)