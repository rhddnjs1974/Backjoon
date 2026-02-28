import sys
import heapq

input = sys.stdin.readline

def update(i, v):
    while (i <= bitn):
        if (v > bit[i]):
            bit[i] = v
        i += (i & (-i))

def query(i):
    r = -1
    while i > 0:
        if (bit[i] > r):
            r = bit[i]
        i -= (i & (-i))
    return r


for testcase in range(int(input())):
    n, m = map(int, input().split())
    bitn = (n + 1)
    bit = [-1] * (bitn + 1)
    
    arr = [[] for _ in range((n + 2))]
    for i in range(n):
        x, y = map(int, input().split())
        arr[(y+1)].append(x)

    arr2 = []   # 상점
    for j in range(m):
        x, y = map(int, input().split())
        arr2.append((x, (y + 1), j))

    maxe = [0] * (n + 2) # 각 k에 대해 만들 수 있는 최대 에너지
    ee = [-1] * (n + 2) #k-1 경우 최대pre
    point = []

    big = [] #상위 k개
    remain = [] #나머지
    sbig = 0 # sum(big)
    
    hubo = 0
    sumhubo = 0
    bb = 0

    for k in range((n+1), 0, -1):
        for x in arr[k]:
            hubo += 1
            sumhubo += x
            heapq.heappush(remain, -x)

        while (len(big) > k):
            v = heapq.heappop(big)
            sbig -= v
            heapq.heappush(remain, -v)

        while (len(big) < k) and (len(remain) > 0):
            v = -heapq.heappop(remain)
            sbig += v
            heapq.heappush(big, v)

        while (len(big) > 0) and (len(remain) > 0 and (-remain[0]) > big[0]):
            a = (-heapq.heappop(remain))
            b = heapq.heappop(big)
            
            sbig += (a-b)
            
            heapq.heappush(big, a)
            heapq.heappush(remain, -b)

        if hubo == k-1:
            ee[k] = sumhubo

        if hubo >= k:
            bb = max(bb,sbig)
            maxe[k] = sbig
            
            point.append((big[0], k, sbig-big[0]))

    for tt in range(1, (n + 2)):
        ee[tt] = max(ee[tt],ee[(tt- 1)])
        
        maxe[tt] = max(maxe[tt],maxe[(tt-1)])

    point.sort()
    arr2.sort()

    ans = [0] * m
    p = 0
    for x, y, z in arr2:
        y = min(y,n+1)

        while p < len(point) and point[p][0] < x:
            update(point[p][1], point[p][2])
            p += 1

        now = bb
        now = max(now,maxe[y])

        if (ee[y] != -1): 
            now = max(now, ee[y]+x)

        xx = query(y)
        if xx != -1:
            now = max(now, xx+x)
            
        ans[z] = now

    print(*ans)