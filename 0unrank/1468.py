N = int(input())

P1 = [1] + [0] * N
P2 = [1] + [0] * N

A = [0] * (N + 2)
B = [0] * (N + 2)

for n in range(1, N + 2):
    deg = n - 1

    A[n] = P1[deg]
    B[n] = (P1[deg] + P2[deg]) // 2

    if n == N+1:
        break

    bn = B[n]
    if bn == 0:
        continue

    max_m = N // n
    comb = [1] * (max_m + 1)
    for m in range(1, max_m + 1):
        comb[m] = comb[m - 1] * (bn + m - 1) // m

    nP1 = [0] * (N + 1)
    nP2 = [0] * (N + 1)

    for d0 in range(N + 1):
        c1 = P1[d0]
        c2 = P2[d0]
        if c1 == 0 and c2 == 0:
            continue

        nP1[d0] += c1
        nP2[d0] += c2

        for m in range(1, max_m + 1):
            d = d0 + n * m
            if d > N:
                break
            nP1[d] += c1 * comb[m]

            if m % 2 == 0:
                nP2[d] += c2 * comb[m]
            else:
                nP2[d] -= c2 * comb[m]

    P1, P2 = nP1, nP2

print(A[N + 1])
