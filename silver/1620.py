import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a = {}
for i in range(1,n+1):
    x = input().rstrip()
    a[str(i)] = x
    a[x] = i

for i in range(m):
    print(a[input().rstrip()])