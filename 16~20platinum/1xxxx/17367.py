def prize(a, b, c):
    if a == b == c:
        return 10000 + a * 1000
    if a == b or a == c:
        return 1000 + a * 100
    if b == c:
        return 1000 + b * 100
    return max(a, b, c) * 100

N = int(input())

dp_next = [[0] * 7 for i in range(7)]

for i in range(1, 7):
    for j in range(1, 7):
        s = 0
        for k in range(1, 7):
            s += prize(i, j, k)
        dp_next[i][j] = s / 6

for i in range(N - 2, 1, -1):
    dp_cur = [[0] * 7 for i in range(7)]
    for j in range(1, 7):
        for k in range(1, 7):
            s = 0.0
            for l in range(1, 7):
                stop = prize(j, k, l)
                cont = dp_next[k][l]
                if stop >= cont:
                    s+= stop
                else:
                    s+= cont
            dp_cur[j][k] = s / 6
    dp_next = dp_cur

ans = 0
for i in range(1, 7):
    for j in range(1, 7):
        ans += dp_next[i][j]
ans /= 36

print(ans)
