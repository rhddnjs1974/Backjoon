import sys
input = sys.stdin.readline

MOD = 1000000007

n = int(input())

arr = [0] * (n+2)

p = 1
for i in range(1, n+1):
    p = (p * 2) % MOD
    arr[i] = pow(p-1, MOD-2, MOD)

ans = 0
for i in range(2, n+1):
    ans += ((i-1) * arr[1]) % MOD
    ans %= MOD

    for j in range(1, n-i+2):
        arr[j] -= ((i-1) * arr[j+1]) % MOD
        arr[j] %= MOD

print(ans)