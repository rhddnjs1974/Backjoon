import sys
input = sys.stdin.readline

seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]

def smallest_digits(length, target):
    if not ok[length][target]:
        return None
    out = []
    rem = target
    for i in range(length):
        left = length-i-1
        for d in range(10):
            need = rem-seg[d]
            if need < 0:
                continue
            if left == 0 and need != 0:
                continue
            if left > 0 and not ok[left][need]:
                continue
            out.append(d)
            rem = need
            break
    return out

def digits_to_int(dig):
    v = 0
    for d in dig:
        v = v * 10 + d
    return v

s = input().rstrip()
n = len(s)
sdigits = [int(c) for c in s]
T = 0
for d in sdigits:
    T += seg[d]

M = 7 * n
ok = [[False] * (M+1) for _ in range(n+1)]
ok[0][0] = True
for i in range(1, n+1):
    for t in range(M+1):
        for d in range(10):
            if t-seg[d] >= 0 and ok[i-1][t-seg[d]]:
                ok[i][t] = True
                break

S_int = digits_to_int(sdigits)

mi = -1
prefix_sum = 0
for i in range(n):
    for d in range(sdigits[i]+1, 10):
        rem = T - prefix_sum - seg[d]
        left = n-i-1
        if rem < 0:
            continue
        if left > 0:
            if not ok[left][rem]:
                continue
            suf = smallest_digits(left, rem)
        else:
            if rem != 0:
                continue
            suf = []
        cand = sdigits[:i] + [d] + suf
        v = digits_to_int(cand)
        if mi == -1 or v < mi:
            mi = v
    prefix_sum += seg[sdigits[i]]

if mi != -1:
    print(mi-S_int)
else:
    msuf = smallest_digits(n, T)
    mv = digits_to_int(msuf)
    if mv == S_int:
        print(10**n)
    else:
        print(10**n - S_int + mv)
