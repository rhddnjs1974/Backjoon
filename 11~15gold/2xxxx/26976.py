import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()

    arr = ['.'] * n
    ans = 0

    for c in 'GH':
        r = -1
        for i in range(n):
            if s[i] != c:
                continue
            if i <= r:
                continue
            p = min(n-1,i+k)
            
            if arr[p] != '.':
                p -= 1
            
            arr[p] = c
            ans += 1
            
            r = p+k

    print(ans)
    print(*arr, sep='')