import sys
input = sys.stdin.readline
import functools
    
for testcase in range(int(input())):
    N = int(input())
    arr = []
    for _ in range(N):
        n,*a = map(int,input().split())
        now = []
        for i in range(n-1,-1,-1):
            if a[i] in now:
                continue
            now.append(a[i])
        arr.append(now)
    

    ans = []
    
    seen = set()
    use = [0]*N
    r= N
    
    while (r):
        f = []
        for i in range(N):
            if use[i]==0:
                f.append(( [u for u in arr[i] if u not in seen], i ))
        
        best = [1e7]
        bestnum = -1
        for i in f:
            if i[0]<best:
                best = i[0][:]
                bestnum = i[1]
        
        use[bestnum]=1
        r -=1
        
        for i in best:
            if i not in seen:
                ans.append(i)
                seen.add(i)
        
    print(*ans)