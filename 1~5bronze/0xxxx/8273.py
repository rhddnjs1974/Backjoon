a = list(map(int,input().split()))
a.sort()
x = a[0]
y = a[1]
z = a[2]

if x==y==z:
    print(2)
elif x**2 + y**2 == z**2:
    print(1)
else:
    print(0)