import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    inc = []
    dec = []

    last_inc = 0
    last_dec = n + 1

    ok = True

    for i in range(n):
        x = p[i]

        if x < last_inc and x > last_dec:
            ok = False
            break

        if x < last_inc:
            dec.append(x)
            last_dec = x
        elif x > last_dec or i == n - 1:
            inc.append(x)
            last_inc = x
        elif x < p[i + 1]:
            inc.append(x)
            last_inc = x
        else:
            dec.append(x)
            last_dec = x


    if not ok:
        print("NO")
    else:
        print("YES")
        if len(inc) == 0:
            print(0)
        else:
            print(len(inc), *inc)

        if len(dec) == 0:
            print(0)
        else:
            print(len(dec), *dec)
