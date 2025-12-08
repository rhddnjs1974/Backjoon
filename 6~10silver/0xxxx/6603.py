import itertools

while(True):
    k, *arr = map(int,input().split())
    if k==0:
        break
    ans = []
    
    for i in itertools.combinations(arr,6):
        ans.append(list(i))
    
    for i in range(len(ans)):
        ans[i].sort()
    ans.sort()
    
    for i in ans:
        print(*i)
    print()