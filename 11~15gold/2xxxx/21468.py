import sys
input = sys.stdin.readline

n = int(input())
rows = []
for i in range(n):
    rows.append(input()[:n])

shifts = [0]*n
groups = [list(range(n))]

for i in range(n):
    if not groups:
        break
    row = rows[i]
    rotations = [row[s:]+row[:s] for s in range(n)]
    total = 0
    for g in groups:
        total += len(g)
    best_s = 0
    best_split = -1
    for s in range(n):
        sr = rotations[s]
        split = 0
        for g in groups:
            v0 = sr[g[0]]
            same = True
            for j in g:
                if sr[j] != v0:
                    same = False
                    break
            if same:
                split += 1
            else:
                split += 2
        if split > best_split:
            best_split = split
            best_s = s
            if best_split == total:
                break
    shifts[i] = best_s
    sr = rotations[best_s]
    new_groups = []
    for g in groups:
        g0 = []
        g1 = []
        for j in g:
            if sr[j] == '0':
                g0.append(j)
            else:
                g1.append(j)
        if len(g0) > 1:
            new_groups.append(g0)
        if len(g1) > 1:
            new_groups.append(g1)
    groups = new_groups

if not groups:
    print("Yes")
    for i in range(n):
        s = shifts[i]
        print(rows[i][s:]+rows[i][:s])
else:
    print("No")
