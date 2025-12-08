import sys
input = sys.stdin.readline

def make_pi(pattern):
    l = len(pattern)
    arr = [0 for _ in range(l)]

    pidx = 0
    for idx in range(1, l):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = arr[pidx - 1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            arr[idx] = pidx

    return arr


def KMP(word, pattern):
    pi_table = make_pi(pattern)

    results = []
    pidx = 0

    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = pi_table[pidx - 1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx - len(pattern) + 2)
                pidx = pi_table[pidx]
            else:
                pidx += 1
    return results

T = input().rstrip()
T = T[::-1]

A = ""
B = ""
ma = 0
for i in T:
    A += i
    B = A[::-1]
    t = make_pi(B)
    ma = max(ma,max(t))
print(ma)