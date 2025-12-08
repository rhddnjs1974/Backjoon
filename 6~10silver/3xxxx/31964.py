import sys
input = sys.stdin.readline

n = int(input())
X = [0] + list(map(int,input().split()))
T = [0] + list(map(int,input().split()))


ans = X[-1]
now = X[-1]

X.append(0)
for a in range(n,-1,-1):
    ans = max(ans+(now-X[a]),T[a])
    now = X[a]
print(ans) 