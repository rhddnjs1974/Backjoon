import sys
input = sys.stdin.readline

for testcase in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    
    if p[0]==n:
        print(*p)
        continue
    
    k = p[0]
    for i in range(n):
        if p[i]==n:
            p[i] = k
            p[0] = n
            break
    
    print(*p)