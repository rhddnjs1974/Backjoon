import sys
input = sys.stdin.readline

m = int(input())
s= set()
for _ in range(m):
    a = input().split()
    if len(a)==1:
        if a[0]=="all":
            for i in range(1,21):
                s.add(i)
        else:
            s = set()
    else:
        b,c = a[0],a[1]
        c = int(c)
        if b=="add":
            s.add(c)
        if b=="remove":
            if c in s:
                s.remove(c)
        if b=="check":
            if c in s:
                print(1)
            else:
                print(0)
        if b=="toggle":
            if c in s:
                s.remove(c)
            else:
                s.add(c)

