#BOJBOOK
import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right

def update(a, d, r, index, v):
    x = a[index]
    a[index] = v
    group = index // r
    
    i = bisect_left(d[group],x)
    d[group][i] = v
    d[group].sort()

def query(a, d, r, start, end, k):
    ans = 0
    if start // r == end // r:
        for i in range(start, end+1):
            if k < a[i]:
                ans +=1
        return ans
    
    while True:
        if k < a[start]:
            ans += 1
        start += 1
        if start % r == 0:
            break

    while True:
        if k < a[end]:
            ans += 1
        end -= 1
        if end % r == r-1:
            break
            
    start_group = start // r
    end_group = end // r
    for i in range(start_group, end_group+1):
        ans += len(d[i]) - bisect_right(d[i],k)

    return ans

n = int(input())
a = list(map(int, input().split())) #array
r = (int)(n ** 0.5) #한 칸의 크기
g = n // r #array 칸수
if n % r != 0:
    g += 1
d = []
for i in range(n):
    if i%r==0:
        d.append([])
    d[i//r].append(a[i])

for i in range(g):
    d[i].sort()


q = int(input())
for _ in range(q):
    s, *t = map(int, input().split())
    if s == 1:
        update(a, d, r, t[0]-1, t[1])
    else:
        print(query(a, d, r, t[0]-1, t[1]-1,t[2]))
