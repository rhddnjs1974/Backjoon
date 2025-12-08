import sys
input = sys.stdin.readline

def getnum(n,x,y):
    if n == 1:
        base = [[1,4],[3,2]]
        return base[x-1][y-1]
    
    half = (2**n) // 2
    small = 4 ** (n - 1)

    if x <= half and y <= half:
        return getnum(n - 1, x, y)
    elif x > half and y > half:
        return getnum(n - 1, x - half, y - half) + small
    elif x > half and y <= half:
        return getnum(n - 1, x - half, y) + small * 2
    else:
        return getnum(n - 1, x, y - half) + small * 3

def getpos(n, d):
    if n == 1:
        if d==1:
            return (1,1)
        if d==4:
            return (1,2)
        if d==3:
            return (2,1)
        if d==2:
            return (2,2)

    half = (2**n) // 2
    small = 4 ** (n - 1)

    if d <= small:
        return getpos(n - 1, d)
    elif d <= small * 2:
        x, y = getpos(n - 1, d - small)
        return (x + half, y + half)
    elif d <= small * 3:
        x, y = getpos(n - 1, d - small * 2)
        return (x + half, y)
    else:
        x, y = getpos(n - 1, d - small * 3)
        return (x, y + half)

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    for i in range(q):
        question = list(input().split())

        if question[0]=="->":
            x,y = question[1],question[2]
            print(getnum(n,int(x),int(y)))
        else:
            d = question[1]
            a1,a2 = getpos(n,int(d))
            print(a1,a2)
        