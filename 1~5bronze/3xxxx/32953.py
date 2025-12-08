n,m = map(int,input().split())
dic = {}
for i in range(n):
    k = int(input())
    arr = list(map(int,input().split()))
    for x in arr:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

ans = 0
for a in dic:
    if dic[a]>=m:
        ans+=1
print(ans)