import itertools

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

ans = 1e9
for i in itertools.combinations(range(n),n//2):
    J = []
    for a in range(n):
        if a not in i:
            J.append(a)
    I = list(i)
    t1 = 0
    t2 = 0
    for a in itertools.permutations(I,2):
        t1 += arr[a[0]][a[1]]
    
    for a in itertools.permutations(J,2):
        t2 += arr[a[0]][a[1]]
    
    ans = min(ans,abs(t1-t2))

print(ans)