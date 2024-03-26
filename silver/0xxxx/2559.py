n,k = map(int,input().split())
arr = list(map(int,input().split()))

ma = -1e9

s=0
for i in range(n):
    if i<k:
        s+=arr[i]
    else:
        s+=arr[i]
        s-=arr[i-k]

    if i>=k-1:
        ma = max(ma,s)

print(ma)