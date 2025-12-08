import itertools

n, m = map(int,input().split())
arr = list(map(int,input().split()))

ans = []
for i in itertools.permutations(arr,m):
    ans.append(list(i))


ans.sort()

for i in range(len(ans)):
    if i!=0 and ans[i-1]==ans[i]:
        continue
    print(*ans[i])