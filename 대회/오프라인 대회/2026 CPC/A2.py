import sys
input = sys.stdin.readline

T = int(input())

for test in range(T):
    N = int(input())
    if N%3!=0:
        print(0)
    else:
        x = N//3
        print(2**x)