import sys
input = sys.stdin.readline
K = int(input())

a = []
for i in range(K):
    x = int(input())
    if x==0:
        a.pop()
    else:
        a.append(x)

print(sum(a))