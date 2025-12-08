import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,W = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    
    if N==1:
        if arr1[0]+arr2[0]<=W:
            print(1)
        else:
            print(2)
        continue
    
    
    dpa = [1e9]*(N+1)
    dpb = [1e9]*(N+1)
    dpc = [1e9]*(N+1)
    ans = 1e9

    dpa[0] = 0
    dpb[0] = 1
    dpc[0] = 1
    
    for i in range(0,N):
        dpa[i+1] = min(dpb[i]+1,dpc[i]+1)
        if arr1[i]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i]+1)
        if i>0 and arr1[i-1]+arr1[i]<=W and arr2[i-1]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i-1]+2)
        
        if i==N-1:
            break
        
        dpb[i+1] = dpa[i+1]+1
        if arr1[i]+arr1[i+1]<=W:
            dpb[i+1] = min(dpb[i+1],dpc[i]+1)
        
        dpc[i+1] = dpa[i+1]+1
        if arr2[i]+arr2[i+1]<=W:
            dpc[i+1] = min(dpc[i+1],dpb[i]+1)
    

    ans = min(ans,dpa[N])

    
    
    
    dpa[1] = 1
    dpb[1] = 2
    if arr2[0]+arr2[1]<=W:
        dpc[1] = 1
    else:
        dpc[1] = 2
    
    for i in range(1,N):
        dpa[i+1] = min(dpb[i]+1,dpc[i]+1)
        if arr1[i]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i]+1)
        if i>1 and arr1[i-1]+arr1[i]<=W and arr2[i-1]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i-1]+2)
        
        if i==N-1:
            break
        
        dpb[i+1] = dpa[i+1]+1
        if arr1[i]+arr1[i+1]<=W:
            dpb[i+1] = min(dpb[i+1],dpc[i]+1)
        
        dpc[i+1] = dpa[i+1]+1
        if arr2[i]+arr2[i+1]<=W:
            dpc[i+1] = min(dpc[i+1],dpb[i]+1)
    
    if(arr1[0]+arr1[N-1]<=W):
        ans = min(ans,dpc[N-1]+1)

    
    dpa[1] = 1
    dpc[1] = 2
    if arr1[0]+arr1[1]<=W:
        dpb[1] = 1
    else:
        dpb[1] = 2
    
    for i in range(1,N):
        dpa[i+1] = min(dpb[i]+1,dpc[i]+1)
        if arr1[i]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i]+1)
        if i>1 and arr1[i-1]+arr1[i]<=W and arr2[i-1]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i-1]+2)
        
        if i==N-1:
            break
        
        dpb[i+1] = dpa[i+1]+1
        if arr1[i]+arr1[i+1]<=W:
            dpb[i+1] = min(dpb[i+1],dpc[i]+1)
        
        dpc[i+1] = dpa[i+1]+1
        if arr2[i]+arr2[i+1]<=W:
            dpc[i+1] = min(dpc[i+1],dpb[i]+1)
    
    if(arr2[0]+arr2[N-1]<=W): 
        ans = min(ans,dpb[N-1]+1)

    
    dpa[1] = 0
    dpc[1] = 1
    dpb[1] = 1
    
    for i in range(1,N):
        dpa[i+1] = min(dpb[i]+1,dpc[i]+1)
        if arr1[i]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i]+1)
        if i>1 and arr1[i-1]+arr1[i]<=W and arr2[i-1]+arr2[i]<=W:
            dpa[i+1] = min(dpa[i+1],dpa[i-1]+2)
        
        if i==N-1:
            break
        
        dpb[i+1] = dpa[i+1]+1
        if arr1[i]+arr1[i+1]<=W:
            dpb[i+1] = min(dpb[i+1],dpc[i]+1)
        
        dpc[i+1] = dpa[i+1]+1
        if arr2[i]+arr2[i+1]<=W:
            dpc[i+1] = min(dpc[i+1],dpb[i]+1)
    
    if(arr1[0]+arr1[N-1]<=W and arr2[0]+arr2[N-1]<=W):
        ans = min(ans,dpa[N-1]+2)
    

    print(ans)