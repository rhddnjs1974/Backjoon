n = int(input())
digits = list(map(int, str(n + 1)))
L = len(digits)

def can(pos, prev, tight):
    if pos == L:
        return 1

    lb = digits[pos] if tight else 0

    for d in range(lb, 10):
        if d == prev:
            continue
        ntight = tight and (d == digits[pos])
        if can(pos + 1, d, ntight):
            return 1
    return 0

if can(0, -1, 1):
    res = []
    prev = -1
    tight = 1
    for pos in range(L):
        if tight:
            lb = digits[pos]
        else:
            lb = 0
            
        for d in range(lb, 10):
            if d == prev:
                continue
            ntight = tight and (d == digits[pos])
            if can(pos + 1, d, ntight):
                print(d,end="")
                prev = d
                tight = ntight
                break
else:
    for i in range(L+1):
        print((i+1)%2,end="")


