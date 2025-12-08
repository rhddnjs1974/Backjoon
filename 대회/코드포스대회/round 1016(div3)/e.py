import sys
input = sys.stdin.readline

def can_make(k, x):
    found = set()
    count = 0

    for num in arr:
        if num < x:
            found.add(num)
        if len(found) == x:
            count += 1
            found.clear() 

    return count >= k

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    l = 0
    r = n+1
    while l<r:
        mid = (l+r)//2
        if can_make(k,mid):
            l = mid + 1
        else:
            r= mid
    print(l-1)