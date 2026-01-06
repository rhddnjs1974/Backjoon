import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def prob_micro(s):
    a, b = s.split('.')
    return int(a) * 1000000 + int(b)

def sign_factor(p):
    f = 1000000 - 2 * p
    if f==0:
        return 0
    elif f<0:
        return -1
    else:
        return 1

signs = [0] * (N + 1)
zero = 0
neg = 0

ps = input().split()
for i in range(1, N + 1):
    s = sign_factor(prob_micro(ps[i-1]))
    signs[i] = s
    if s == 0: 
        zero += 1
    elif s < 0: 
        neg += 1

if zero:
    print("SAME")
elif (neg & 1) == 0:
    print("DEAD")
else: 
    print("ALIVE")

for i in range(M):
    idx, p = input().split()
    idx = int(idx)
    ns = sign_factor(prob_micro(p))

    os = signs[idx]
    if os == 0: 
        zero -= 1
    elif os < 0:
        neg -= 1

    signs[idx] = ns
    if ns == 0: 
        zero += 1
    elif ns < 0: 
        neg += 1

    if zero:
        print("SAME")
    elif (neg & 1) == 0:
        print("DEAD")
    else: 
        print("ALIVE")
