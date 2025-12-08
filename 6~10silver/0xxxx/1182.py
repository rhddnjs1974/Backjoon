def bt(now,x):

    global n,s,ans
    if x==n:
        if now==s:
            ans+=1
        return
    
    bt(now+arr[x],x+1)
    bt(now,x+1)
    
    
ans=0
n, s = map(int,input().split())
arr = list(map(int,input().split()))

bt(arr[0],1)
bt(0,1)

if s==0:
    print(ans-1)
else:
    print(ans)