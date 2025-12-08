import sys
input = sys.stdin.readline

T= int(input())

for i in range(T):
    n = int(input())
    dic = {}
    for i in range(n):
        a,b = input().split()
        if b in dic:
            dic[b] +=1
        else:
            dic[b] = 1
    k=1
    for i in dic:
        k*=(dic[i]+1)
    print(k-1)
