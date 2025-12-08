import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a,b,c,d = map(int,input().split())
    x=0
    for x in range(1,abs(d)+1):
        if d%x!=0:
            continue

        if a*x**3+b*x**2+c*x+d==0:
            break
        if -a*x**3+b*x**2-c*x+d==0:
            x = -x
            break

    a2 = a
    b2 = b+a*x
    c2 = c+b*x+a*x**2

    ans = set()

    D = b2**2-4*a2*c2
    if D<0:
        ans.add(x)
    else:
        ans.add(x)
        ans.add((-b2+(b2**2-4*a2*c2)**(0.5))/(2*a2))
        ans.add((-b2-(b2**2-4*a2*c2)**(0.5))/(2*a2))

    ans = list(ans)
    ans.sort()

    print(*ans)