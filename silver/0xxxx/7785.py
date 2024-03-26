import sys
input = sys.stdin.readline

n = int(input())
a = set()
for i in range(n):
    x,y = input().split()
    if y=="enter":
        a.add(x)
    else:
        a.remove(x)

a = list(a)
a.sort()
a.reverse()
for i in a:
    print(i)