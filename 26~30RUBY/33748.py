a = []
m =90
J = 25
for i in range(m):
    for j in range(1,J):
        a.append((i**2+j**2,i,j))
a.sort()
s = set()

n = int(input())


for _ in range(n):
    