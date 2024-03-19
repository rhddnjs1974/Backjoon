C = int(input())
for i in range(C):
    N,*arr = map(int,input().split())
    av = sum(arr)/N
    ans = 0
    for i in arr:
        if i >av:
            ans+=1

    print("%.3f"%(100*ans/N)+"%")