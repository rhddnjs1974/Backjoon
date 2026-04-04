import sys
input = sys.stdin.readline

def build_distinct(vals, prev):
    arr = vals[:]
    res = []
    cur = prev
    
    while arr:
        ok = 0
        for i in range(len(arr)):
            x = arr[i]
            
            if x == cur+1:
                continue
            
            if len(arr) == 2:
                y = arr[1-i]
                if y == x+1:
                    continue
                
            res.append(x)
            cur = x
            arr.pop(i)
            ok = 1
            break
        
        if ok == 0:
            return None
        
    return res

def can(state, prev):
    key = (state, prev)
    
    if key in memo:
        return memo[key]

    total = 0
    one = 1
    
    for x in state:
        total += x
        if x > 1:
            one = 0

    if total == 0:
        memo[key] = 1
        return 1

    if one == 1:
        arr = []
        for i in range(len(vals)):
            if state[i] == 1:
                arr.append(vals[i])
                
        if build_distinct(arr, prev) is None:
            memo[key] = 0
            return 0
        memo[key] = 1
        return 1

    for i in range(len(vals)):
        if state[i] == 0:
            continue
        if vals[i] == prev+1:
            continue
        nxt = list(state)
        nxt[i] -= 1
        if can(tuple(nxt), vals[i]) == 1:
            memo[key] = 1
            return 1

    memo[key] = 0
    return 0

def build(state, prev):
    total = 0
    one = 1
    for x in state:
        total += x
        if x > 1:
            one = 0

    if total == 0:
        return []

    if one == 1:
        arr = []
        for i in range(len(vals)):
            if state[i] == 1:
                arr.append(vals[i])
        return build_distinct(arr, prev)

    for i in range(len(vals)):
        if state[i] == 0:
            continue
        if vals[i] == prev+1:
            continue
        nxt = list(state)
        nxt[i] -= 1
        nxt = tuple(nxt)
        if can(nxt, vals[i]) == 1:
            res = [vals[i]]
            tail = build(nxt, vals[i])
            for x in tail:
                res.append(x)
            return res

    return []

n = int(input())
a = list(map(int, input().split()))
a.sort()

vals = []
cnts = []
for x in a:
    if len(vals) == 0 or vals[-1] != x:
        vals.append(x)
        cnts.append(1)
    else:
        cnts[-1] += 1

vals = tuple(vals)
state = tuple(cnts)
memo = {}
ans = build(state, -2000000000)

for i in range(n):
    print(ans[i], end=" ")