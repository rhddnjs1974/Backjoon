MOD13 = 10**13

def fib_mod(n, mod):
    a = 0
    b = 1

    for bit in bin(n)[2:]:
        two_b_minus_a = (2*b - a) % mod
        d = (a * two_b_minus_a) % mod
        e = (a*a + b*b) % mod
        if bit == '0':
            a = d
            b = e
        else:
            a = e
            b = (d + e) % mod
    return a

N = int(input().strip())
if N >= MOD13:
    print(-1)
    exit(0)
    
mod = 10**3
period = 15 * 10**2 

target = N % mod

cand = []

a = 0  
b = 1  
if a == target:
    cand.append(0)
if b == target:
    cand.append(1)

for i in range(2, period):
    c = (a + b) % mod
    a = b
    b = c
    if b == target:
        cand.append(i)

for _ in range(3, 13):
    next_mod = mod * 10
    next_target = N % next_mod
    next_period = period * 10
    
    next_cand = []

    for base in cand:
        for m in range(10):
            idx = base + period * m
            if fib_mod(idx, next_mod) == next_target:
                next_cand.append(idx)

    if next_cand:
        next_cand = sorted(set(x % next_period for x in next_cand))

    cand = next_cand
    mod = next_mod
    period = next_period

    if not cand:
        break

if cand:
    print(min(cand))
else:
    print(-1)