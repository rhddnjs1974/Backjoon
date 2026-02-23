N, K =map(int,input().split())

arr = []
arr2 = [0]*K
for i in range(N):
    now = list(map(int,input().split()))
    for x in range(K):
        if arr2[x]==now[x]:
            arr2[x]+=0.0001
        elif arr2[x]<now[x]:
            arr2[x]=now[x]
    
    arr.append(now)


ans = 0
for i in range(N):
    for j in range(K):
        if arr[i][j]>=arr2[j]:
            ans+=1
            break

print(ans)