import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    dict = {}
    for i in range(n):
        if arr[i] in dict:
            dict[arr[i]].append(i+1)
        else:
            dict[arr[i]] = [i+1]

    vals = sorted(dict.keys(), reverse=True)

    ff = [0] * (n+1)
    for i in range(1, n+1):
        j = i
        while j <= n:
            ff[j] += 1
            j += j & -j

    rem = n
    ans = 0

    for v in vals:
        d = dict[v]
        l = len(d)

        if rem <= 2:
            break

        for x in d:
            y = x
            while y <= n:
                ff[y] -= 1
                y += y & -y

        small = rem-l

        left = [0] * l
        right = [0] * l

        for i in range(l):
            x = d[i]-1
            s = 0
            while x > 0:
                s += ff[x]
                x -= x & -x
            left[i] = s
            right[i] = small-s

        pp = [0] * (l+1)
        for i in range(l):
            pp[i+1] = pp[i]+left[i]

        ss = [0] * (l+1)
        for i in range(l-1, -1, -1):
            ss[i] = ss[i+1]+right[i]

        keep = 0
        if small < 2:
            keep = 2-small

        now = 10**30

        if keep == 0:
            for i in range(l+1):
                now = min(now, pp[i]+ss[i])
        else:
            for i in range(l-keep+1):
                now = min(now, pp[i]+ss[i+keep])

        ans += now
        rem = small+keep

    print(ans)