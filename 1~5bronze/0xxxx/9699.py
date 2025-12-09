n = int(input())
for i in range(1,n+1):
    arr = list(map(int,input().split()))
    print("Case #"+str(i)+":",max(arr))