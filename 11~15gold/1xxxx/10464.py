import sys
input = sys.stdin.readline

def xor_1_to_n(n):
    if n%4==0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n+1
    if n % 4 == 3:
        return 0

T = int(input())
for _ in range(T):
    s,f = map(int,input().split())
    ans = xor_1_to_n(s-1)^xor_1_to_n(f)
    print(ans)