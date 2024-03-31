import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    U = []
    D = []

    now = 1
    flag=0
    for i in A:
        if i ==now:
            now+=1
            continue

        if len(U)==0:
            U.append(i)
        elif U[-1] == i-1:
            U.append(i)
        elif len(D)==0:
            D.append(i)
        elif D[-1] == i-1:
            D.append(i)
        else:
            if U[0]==now:
                now = U[-1]+1
                U = [i]
            elif D[0]==now:
                now = D[-1]+1
                D = [i]
            else:
                print("NO")
                flag=1
                break
    if flag==0:
        print("YES")


