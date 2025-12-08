def merge_sort(p,r):
    if (p<r):
        q = int((p+r)/2)
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(p,q,r)

def merge(p,q,r):
    global cnt,K,ans
    i = p
    j = q+1
    t = -1
    while(i<=q and j<=r):
        if (A[i]<=A[j]):
            tmp[t] = A[i]
            t+=1
            i+=1
        else:
            tmp[t] = A[j]
            t+=1
            j+=1
    
    while(i<=q):
        tmp[t] = A[i]
        t+=1
        i+=1
    
    while(j<=r):
        tmp[t] = A[j]
        t+=1
        j+=1
    
    i = p
    t = -1
    
    while(i<=r):
        A[i] = tmp[t]
        i+=1
        t+=1
        cnt+=1
        if cnt==K:
            ans = A[i-1]

N,K = map(int,input().split())
A = list(map(int,input().split()))
tmp = [0]*N



ans = 0
cnt = 0
merge_sort(0,N-1)
if ans==0:
    print(-1)
else:
    print(ans)