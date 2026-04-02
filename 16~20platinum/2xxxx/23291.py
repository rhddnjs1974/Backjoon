import sys
input = sys.stdin.readline

def first_stack(arr):
    n = len(arr)
    cols = [[arr[1], arr[0]]]
    for i in range(2, n):
        cols.append([arr[i]])

    w = 1
    h = 2
    while len(cols)-w >= h:
        for i in range(h):
            extra = []
            for j in range(w-1, -1, -1):
                extra.append(cols[j][i])
            cols[w+i].extend(extra)
        cols = cols[w:]
        w, h = h, w+1
    return cols

def second_stack(arr):
    n = len(arr)
    half = n//2
    quarter = n//4

    cols = []
    for i in range(half):
        cols.append([arr[half+i], arr[half-1-i]])

    res = []
    for i in range(quarter):
        col = cols[quarter+i][:]
        t = cols[quarter-1-i]
        for j in range(len(t)-1, -1, -1):
            col.append(t[j])
        res.append(col)
    return res

def balance(cols):
    m = len(cols)
    diff = []
    for i in range(m):
        diff.append([0] * len(cols[i]))

    for i in range(m):
        for j in range(len(cols[i])):
            if i+1 < m and j < len(cols[i+1]):
                d = abs(cols[i][j]-cols[i+1][j])//5
                if d > 0:
                    if cols[i][j] > cols[i+1][j]:
                        diff[i][j] -= d
                        diff[i+1][j] += d
                    else:
                        diff[i][j] += d
                        diff[i+1][j] -= d
            if j+1 < len(cols[i]):
                d = abs(cols[i][j]-cols[i][j+1])//5
                if d > 0:
                    if cols[i][j] > cols[i][j+1]:
                        diff[i][j] -= d
                        diff[i][j+1] += d
                    else:
                        diff[i][j] += d
                        diff[i][j+1] -= d

    for i in range(m):
        for j in range(len(cols[i])):
            cols[i][j] += diff[i][j]
    return cols

def flatten(cols):
    arr = []
    for i in range(len(cols)):
        for j in range(len(cols[i])):
            arr.append(cols[i][j])
    return arr

def organize(arr):
    mi = min(arr)
    for i in range(len(arr)):
        if arr[i] == mi:
            arr[i] += 1

    cols = first_stack(arr)
    cols = balance(cols)
    arr = flatten(cols)

    cols = second_stack(arr)
    cols = balance(cols)
    arr = flatten(cols)

    return arr

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
while max(arr)-min(arr) > k:
    arr = organize(arr)
    ans += 1

print(ans)