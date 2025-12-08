for _ in range(int(input())):
    a,b = map(int,input().split())
    ar = []
    for i in range(a):
        ar.append(input())
    arr = []
    arr.append([0]*(b+2))
    for i in ar:
        t = [0]
        for x in i:
            t.append(int(x))
        t.append(0)
        arr.append(t)
    arr.append([0]*(b+2))
    
    ans = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            if arr[i][j]!=0:
                ans+=2
            if arr[i][j]>arr[i-1][j]:
                ans+= arr[i][j]-arr[i-1][j]
            if arr[i][j]>arr[i][j-1]:
                ans+= arr[i][j]-arr[i][j-1]
            if arr[i][j]>arr[i+1][j]:
                ans+= arr[i][j]-arr[i+1][j]
            if arr[i][j]>arr[i][j+1]:
                ans+= arr[i][j]-arr[i][j+1]
    
    print(ans)