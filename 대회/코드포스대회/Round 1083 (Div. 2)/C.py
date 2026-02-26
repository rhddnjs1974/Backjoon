import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    left = [-1] * n
    right = [-1] * n
    parent = [-1] * n

    st = []
    for i in range(n):
        last = -1
        while st and a[st[-1]] < a[i]:
            last = st.pop()
        if st:
            parent[i] = st[-1]
            right[st[-1]] = i
        if last != -1:
            parent[last] = i
            left[i] = last
        st.append(i)

    root = st[0]
    while parent[root] != -1:
        root = parent[root]

    order = []
    q = [root]
    while q:
        u = q.pop()
        order.append(u)
        if left[u] != -1:
            q.append(left[u])
        if right[u] != -1:
            q.append(right[u])

    dp = [0] * n
    for u in order[::-1]:
        v = 0
        if left[u] != -1 and v < dp[left[u]]:
            v = dp[left[u]]
        if right[u] != -1 and v < dp[right[u]]:
            v = dp[right[u]]
        dp[u] = v + 1

    print(n - dp[root])