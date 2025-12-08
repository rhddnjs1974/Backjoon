import sys
input = sys.stdin.readline

def cost(target):
    chars = []
    lens = []
    for c in s:
        if len(chars) !=0 and chars[-1] == c:
            lens[-1] += 1
        else:
            chars.append(c)
            lens.append(1)

    l, r = 0, len(chars) - 1
    bad = '1' if target == '0' else '0'
    remain = sum(1 for c in chars if c == bad)

    bad_r = 0
    peel = 0

    while remain > 0:
        if chars[l] == bad:
            bad_r += lens[l]
            l += 1
            remain -= 1
            continue
        if chars[r] == bad:
            bad_r += lens[r]
            r -= 1
            remain -= 1
            continue
        
        if lens[l] < lens[r]:
            m = lens[l]
        else:
            m = lens[r]
            
        peel += m
        
        if lens[l] <= lens[r]:
            l += 1
        else:
            r -= 1

    return bad_r + 2 * peel

T = int(input().strip())

for _ in range(T):
    n = int(input())
    s = input().strip()
    print((min(cost('0'), cost('1'))))
