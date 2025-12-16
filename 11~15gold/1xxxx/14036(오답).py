from collections import deque
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
notes = [0] * (N+1)
for i in range(1, N+1):
    a,b = map(int, input().split())
    notes[i] = (a,b)


def gen(pos, last, cur, s):
    if pos == D:
        s.append(tuple(cur))
        return
    
    for p in range(last + 1, 13):
        cur.append(p)
        gen(pos + 1, p, cur, s)
        cur.pop()
            
def can(X):
    start_states = []
    gen(0, 0, [], start_states)

    q = deque()
    visited = set()

    for s in start_states:
        if notes[1][1] in s:
            q.append((1, s))
            visited.add((1, s))

    while q:
        i, tuning = q.popleft()
        if i == N:
            return True

        gap = notes[i + 1][0] - notes[i][0]
        if X>0:
            max_ops = int(gap // X)
        else:
            max_ops = 100
        
        states = {tuning}
        
        for a in range(max_ops):
            new_states = set(states)
            for t in states:
                for d in range(D):
                    if d==0:
                        low = 1
                    else:
                        low = t[d - 1] + 1
                    
                    if d<D-1:
                        high = t[d + 1] - 1
                    else:
                        high = 12
                        
                    for p in range(low, high + 1):
                        if p != t[d]:
                            nt = list(t)
                            nt[d] = p
                            new_states.add(tuple(nt))
            states = new_states

        for t in states:
            if notes[i + 1][1] in t:
                nxt = (i + 1, t)
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
                    
    return False

lo = 0
hi = 0
for i in range(1,N):
    hi = max(notes[i+1][0] - notes[i][0],hi)

for _ in range(100):
    mid = (lo + hi) / 2
    if can(mid):
        lo = mid
    else:
        hi = mid

if N <= D:
    print("0.00")
else:
    print("%.2f"%(lo))
