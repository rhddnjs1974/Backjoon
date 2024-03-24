import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dic = {}
for i in range(N):
    a,b = input().split()
    a = a.rstrip()
    b = b.rstrip()
    dic[a] = b
for i in range(M):
    a = input().rstrip()
    print(dic[a])