import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
if n%2 == 1:
    print(0)
else:
    p = [0] * (n+1)
    for i in range(n):
        if s[i] == '(':
            p[i+1] = p[i]+1
        else:
            p[i+1] = p[i]-1

    suf = [0] * (n+1)
    suf[n] = p[n]
    for i in range(n-1, -1, -1):
        suf[i] = min(suf[i+1], p[i])

    ans = 0
    pre = 0

    if p[n] == 2:
        for j in range(1, n+1):
            if pre < 0:
                break
            if s[j-1] == '(' and suf[j] >= 2:
                ans += 1
            pre = min(pre, p[j])
    elif p[n] == -2:
        for j in range(1, n+1):
            if pre < 0:
                break
            if s[j-1] == ')' and suf[j] >= -2:
                ans += 1
            pre = min(pre, p[j])

    print(ans)
