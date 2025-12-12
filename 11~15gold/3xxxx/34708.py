n,k = map(int,input().split())
if k<n*2:
    print(-1)
elif k==n*2:
    print(n*2-1)
else:
    print(n*2)