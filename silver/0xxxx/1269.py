import sys
input = sys.stdin.readline
a,b = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

x = set()
y = set()

for i in A:
    x.add(i)
for j in B:
    y.add(j)
    if j in x:
        x.remove(j)
for i in A:
    if i in y:
        y.remove(i)

for i in y:
    x.add(i)

print(len(x))