import sys
input = sys.stdin.readline

def roll_e(d):
    t, b, n, s, e, w = d
    return (w, e, n, s, t, b)

def roll_w(d):
    t, b, n, s, e, w = d
    return (e, w, n, s, b, t)

def roll_n(d):
    t, b, n, s, e, w = d
    return (s, n, t, b, e, w)

def roll_s(d):
    t, b, n, s, e, w = d
    return (n, s, b, t, e, w)

t = int(input())
for _ in range(t):
    line = input()
    die = (1, 6, 5, 2, 4, 3)
    x = 0
    y = 0
    sign = 1
    num = 0
    for c in line:
        if c == '.':
            break
        if '0' <= c <= '9':
            num *= 10
            num += int(c)
        elif c == '+':
            sign = 1
        elif c == '-':
            sign = -1
        elif c == 'X':
            cnt = max(num, 1)
            x += sign * cnt
            for _ in range(cnt % 4):
                if sign == 1:
                    die = roll_e(die)
                else:
                    die = roll_w(die)
            num = 0
        elif c == 'Y':
            cnt = max(num, 1)
            y += sign * cnt
            for _ in range(cnt % 4):
                if sign == 1:
                    die = roll_n(die)
                else:
                    die = roll_s(die)
            num = 0
    print(f"position ({x},{y}), {die[0]} dots")
