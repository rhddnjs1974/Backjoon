import sys
input = sys.stdin.readline

n = int(input())
x = []
for i in range(n):
    a = input().rstrip()
    if a=="pop":
        if x:
            print(x.pop())
        else:
            print(-1)
    elif a=="size":
        print(len(x))
    elif a=="empty":
        if x:
            print(0)
        else:
            print(1)
    elif a=="top":
        if x:
            print(x[-1])
        else:
            print(-1)
    else:
        b,c = a.split()
        x.append(c)