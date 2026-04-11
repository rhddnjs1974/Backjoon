import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]

S = [0] * (n+1)
for i in range(n):
    S[i+1] = S[i]+A[i]

NEG = -(1 << 62)
INF = 1 << 62

P_l = [None] * (n+1)
P_k = [None] * (n+1)
P_pj = [None] * (n+1)
P_pi = [None] * (n+1)

P_l[0] = [NEG]
P_k[0] = [0]
P_pj[0] = [-1]
P_pi[0] = [-1]

cand_l = [INF] * (n+2)
cand_pj = [-1] * (n+2)
cand_pi = [-1] * (n+2)

for i in range(1, n+1):
    Si = S[i]
    used_nk = []
    for j in range(i):
        d = Si-S[j]
        idx = bisect_left(P_l[j], d)-1
        if idx < 0:
            continue
        nk = P_k[j][idx]+1
        if cand_l[nk] > d:
            if cand_l[nk] == INF:
                used_nk.append(nk)
            cand_l[nk] = d
            cand_pj[nk] = j
            cand_pi[nk] = idx

    used_nk.sort()
    fk = []
    fl = []
    fpj = []
    fpi = []
    for k in used_nk:
        l = cand_l[k]
        while fl and fl[-1] >= l:
            fk.pop()
            fl.pop()
            fpj.pop()
            fpi.pop()
        fk.append(k)
        fl.append(l)
        fpj.append(cand_pj[k])
        fpi.append(cand_pi[k])

    for k in used_nk:
        cand_l[k] = INF
        cand_pj[k] = -1
        cand_pi[k] = -1

    P_l[i] = fl
    P_k[i] = fk
    P_pj[i] = fpj
    P_pi[i] = fpi

m = P_k[n][-1]
idx = len(P_k[n])-1
cuts = []
cur_i = n
while cur_i > 0:
    j = P_pj[cur_i][idx]
    pi_idx = P_pi[cur_i][idx]
    if j > 0:
        cuts.append(j)
    cur_i = j
    idx = pi_idx
cuts.reverse()

print(m)
for x in cuts:
    print(x, end=" ")
print()
