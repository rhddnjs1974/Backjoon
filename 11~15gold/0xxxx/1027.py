n = int(input())
arr = list(map(int,input().split()))

ans = 0
for i in range(n):
    nowans= 0
    m = 1e10
    for j in range(i-1,-1,-1):
        x = i-j
        y = arr[i]-arr[j]
        nowm = y/x
        if nowm<m:
            m = nowm
            nowans +=1
    
    m = -1e10
    for j in range(i+1,n):
        x = j-i
        y = arr[j]-arr[i]
        nowm = y/x
        if nowm>m:
            m = nowm
            nowans +=1
        
    ans = max(ans,nowans)
print(ans)