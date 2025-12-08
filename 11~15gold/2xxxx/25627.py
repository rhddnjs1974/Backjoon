for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = []
    if n%2==1:
        for i in range(1,n+1):
            if i not in arr:
                ans.append(i)
        print(n,len(ans))
        print(*ans)
    else:
        if 1 in arr:
            ans.append(1)
        for i in range(2,n+1):
            if i not in arr:
                ans.append(i)
        print(n,len(ans))
        print(*ans)