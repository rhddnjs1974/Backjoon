import sys
input = sys.stdin.readline

def bit_add(bit, n, i, v):
    while i <= n:
        bit[i] += v
        i += i & -i

def bit_sum(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

N = int(input())
pos = [[] for _ in range(6)]

wr = [0] * (N+1)
wc = [0] * (N+1)
for i in range(1, N+1):
    wr[i] = i * (N-i+1)
    wc[i] = i * (N-i+1)

single = [0] * 6

for r in range(1, N+1):
    row = list(map(int, input().split()))
    w = wr[r]
    for c in range(1, N+1):
        v = row[c-1]
        pos[v].append((r, c))
        single[v] += w * wc[c]

C = N*(N+1) / 2.0
den = C*C
    
ans = 0.0

for k in range(1, 6):
    cells = pos[k]
    cells.sort()

    bitA = [0] * (N+1)
    bitB = [0] * (N+1)
    totalB = 0

    pair_numer = 0

    for r, c in cells:
        prefA = bit_sum(bitA, c)
        prefB = bit_sum(bitB, c)

        left = (N - c + 1) * prefA
        right = c * (totalB - prefB)

        pair_numer += (N - r + 1) * (left + right)

        bit_add(bitA, N, c, r * c)
        addB = r * (N - c + 1)
        bit_add(bitB, N, c, addB)
        totalB += addB

    ans += k * (single[k] + 2 * pair_numer) / den

print(ans)