import sys
input = sys.stdin.readline

n = int(input())
x = []
for i in range(n):
    a = input().rstrip()
    if a=="2":
        if x:
            print(x.pop())
        else:
            print(-1)
    elif a=="3":
        print(len(x))
    elif a=="4":
        if x:
            print(0)
        else:
            print(1)
    elif a=="5":
        if x:
            print(x[-1])
        else:
            print(-1)
    else:
        b,c = a.split()
        x.append(c)