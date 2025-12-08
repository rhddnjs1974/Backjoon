N, K = map(int, input().split())
t = 0

prime = [1] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if prime[j] != 0:
            prime[j] = 0
            t += 1
            if t == K:
                print(j)