import sys
input = sys.stdin.readline

a = int(input())
if 400%a==0:
    print(400//a)
else:
    print(-1)