import sys
input = sys.stdin.readline

n,k,m = map(int,input().split())

for _ in range(m):
    for i in range(1,k+1):
        print(i,end=" ")
    print(flush=True)
    arr = list(map(int,input().split()))