import sys
input = sys.stdin.readline

L, R = map(int, input().split())
print((R-L+1) * (L+R) // 2 % 9)
