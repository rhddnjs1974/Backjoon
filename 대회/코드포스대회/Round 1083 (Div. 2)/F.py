import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for testcase in range(int(input())):
    n, m = map(int, input().split())
    mm = (m - 1)
    nn = (n - 1)
    f = ((nn * mm) + 1)
    
    parent = []
    for i in range(f):
        parent.append(i)
    dp = [0] * f

    for i in range(1, n):
        arr = list(map(int, input().split()))
        for j in range(1, m + 1):
            if j == 1:
                left = 0
            else:
                left = (((i-1) * mm) + (j - 1))
            
            if j == m:
                right = 0
            else:
                right = (((i-1) * mm) + j)
                
            dp[right] = (dp[right] + arr[j - 1])
            dp[left] = (dp[left] - arr[j - 1])

    for i in range(1, n + 1):
        arr = list(map(int, input().split()))
        for j in range(1, m):
            if i == 1:
                up = 0
            else:
                up = (((i-2) * mm) + j)
                
            if i == n:
                down = 0
            else:
                down = (((i-1) * mm) + j)
                
            dp[down] = (dp[down] + arr[j - 1])
            dp[up] = (dp[up] - arr[j - 1])

    for i in range(1, n):
        s = input().rstrip()
        for j in range(1, m + 1):
            if s[j - 1] == "0":
                if j == 1:
                    left = 0
                else:
                    left = (((i-1) * mm) + (j - 1))
                
                if j == m:
                    right = 0
                else:
                    right = (((i-1) * mm) + j)
                    
                union(left, right)

    for i in range(1, n + 1):
        s = input().rstrip()
        for j in range(1, m):
            if s[j - 1] == "0":
                if i == 1:
                    up = 0
                else:
                    up = (((i-2) * mm) + j)
                    
                if i == n:
                    down = 0
                else:
                    down = (((i-1) * mm) + j)
                    
                union(up, down)

    for i in range(f):
        parent[i] = find(i)

    DP2 = [0] * f

    for i in range(1, f):
        DP2[parent[i]] = (DP2[parent[i]] + dp[i])

    ans = 0
    for i in range(1, f):
        if parent[i] == i and i != parent[0] and DP2[i] > 0:
            ans += DP2[i]

    print(ans)