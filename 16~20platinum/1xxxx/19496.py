import sys
input = sys.stdin.readline

def primeList(n):
    n += 1
    arr = [0, 0] + [1] * n

    for i in range(2, int(n**0.5) + 1):
        if arr[i] == 1:
            for j in range(i * 2, n + 1, i):
                arr[j] = 0

    return arr

n = int(input().strip())

if n == 1:
    print("! 1")
    sys.stdout.flush()
    sys.exit()

is_prime = primeList(n)

L = 1
for p in range(2, n + 1):
    if is_prime[p] == 1:
        pk = p
        while pk * p <= n:
            pk *= p
        L *= pk

x = L - 1
print("? " + str(x))
sys.stdout.flush()

r = int(input())

print("! " + str(r + 1))
sys.stdout.flush()
