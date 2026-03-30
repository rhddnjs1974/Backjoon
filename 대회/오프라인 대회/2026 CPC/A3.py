import sys
input = sys.stdin.readline

T = int(input())

for test in range(T):
    N,S = map(int,input().split())
    if S==N+10000000:
        print("Yes")
    else:
        print("No")