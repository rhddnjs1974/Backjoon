import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    pq = []
    for i in C:
        heapq.heappush(pq,i)

    if K > 1:
        r = (N - 1) % (K - 1)
        if r != 0:
            for i in range((K - 1) - r):
                heapq.heappush(pq, 0)

    ans = 0

    while len(pq) > 1:
        s = 0
        for i in range(K):
            s += heapq.heappop(pq)
        ans += s
        heapq.heappush(pq, s)

    print(ans)
