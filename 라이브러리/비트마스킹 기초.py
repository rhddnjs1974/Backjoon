import sys
input = sys.stdin.readline

m = int(input())
s = 0

for _ in range(m):
    a = input().split()
    if len(a)==2:
        f,x = a[0],a[1]
        x=int(x)
        if f=="add":
            s = s|(1<<x)
        elif f=="remove":
            s = s&~(1<<x)
        elif f=="check":
            if s&(1<<x):
                print(1)
            else:
                print(0)
        elif f=="toggle":
            s = s^(1<<x)
    else:
        if a[0]=="all":
            s = 0b111111111111111111111
        else:
            s = 0
