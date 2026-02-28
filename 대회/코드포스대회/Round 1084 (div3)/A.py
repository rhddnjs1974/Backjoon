import sys
input = sys.stdin.readline

for testcase in range(int(input())):
    n = int(input().strip())
    arr = list(map(int, input().split()))

    win = set()

    for s in range(n):
        b = arr[:]
        x = sum(b)
        
        now = s
        last = -1

        while x > 0:
            if b[now] > 0:
                b[now] -= 1
                x -= 1
                last = now
                
            now += 1
            if now == n:
                now = 0

        win.add(last)

    print(len(win))