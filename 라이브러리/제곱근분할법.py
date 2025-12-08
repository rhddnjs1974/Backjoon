#BOJBOOK
import sys
input = sys.stdin.readline

def update(a, d, r, index, v):
    a[index] = v
    group = index // r
    start = group * r
    end = start + r
    if end > len(a):
        end = len(a)
    d[group] = a[start]
    for i in range(start, end):
        if d[group] > a[i]:
            d[group] = a[i]

def query(a, d, r, start, end):
    ans = a[start]
    if start // r == end // r:
        for i in range(start, end+1):
            if ans > a[i]:
                ans = a[i]
        return ans
    
    while True:
        if ans > a[start]:
            ans = a[start]
        start += 1
        if start % r == 0:
            break

    while True:
        if ans > a[end]:
            ans = a[end]
        end -= 1
        if end % r == r-1:
            break
            
    start_group = start // r
    end_group = end // r
    for i in range(start_group, end_group+1):
        if ans > d[i]:
            ans = d[i]

    return ans

n = int(input())
a = list(map(int, input().split())) #array
r = (int)(n ** 0.5) #한 칸의 크기
g = n // r #array 칸수
if n % r != 0:
    g += 1
d = [0] * g
for i in range(n):
    if i % r == 0:
        d[i//r] = a[i]
    else:
        if d[i//r] > a[i]:
            d[i//r] = a[i]

q = int(input())
for _ in range(q):
    t, t1, t2 = map(int, input().split())
    if t == 1:
        update(a, d, r, t1-1, t2)
    else:
        print(query(a, d, r, t1-1, t2-1))
