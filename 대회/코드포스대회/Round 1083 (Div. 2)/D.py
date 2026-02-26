import sys
input = sys.stdin.readline

for testcase in range(int(input())):
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

    depth = [0] * n
    depth[root] = 1
    stack = [root]
    best = 1

    while stack:
        u = stack.pop()

        v = left[u]
        if v != -1:
            depth[v] = depth[u] + 1
            if best < depth[v]:
                best = depth[v]
            stack.append(v)
            
        v = right[u]
        if v != -1:
            depth[v] = depth[u] + 1
            if best < depth[v]:
                best = depth[v]
            stack.append(v)

    print(n - best)