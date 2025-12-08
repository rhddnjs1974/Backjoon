import sys
input = sys.stdin.readline

islogin = 0
ans = 0
N = int(input())
for _ in range(N):
    S = input().rstrip()
    if S=="login":
        islogin = 1
    elif S=="logout":
        islogin = 0
    elif S=="private" and islogin == 0:
        ans += 1
print(ans)