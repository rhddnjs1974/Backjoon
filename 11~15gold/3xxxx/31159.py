import sys
input = sys.stdin.readline

n = int(input())

S = []
diff_s = 0

for i in range(n*2):
    a, b = map(int, input().split())

    diff_s += max(a,b) - min(a,b)
    S.append(a + b)

S.sort()

ss = 0
for i in range(n):
    ss += S[n*2-1-i] - S[i]

print((diff_s + ss) //2)
