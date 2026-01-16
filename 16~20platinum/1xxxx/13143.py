import sys
input = sys.stdin.readline

def pair_prob(a, b):
    x = 0
    if a[0] > b[0]: x += 1
    if a[0] > b[1]: x += 1
    if a[1] > b[0]: x += 1
    if a[1] > b[1]: x += 1
    return x * 0.25

N = int(input().strip())
girls = []
for i in range(N):
    S, H = map(int, input().split())
    girls.append((S, H))

girls.sort(key=lambda x: (x[0] + x[1], x[0], x[1]))

ans = 0
for i in range(N):
    ai = girls[i]
    for j in range(i):
        ans += pair_prob(ai, girls[j])

print(ans)