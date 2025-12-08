import sys
input = sys.stdin.readline

N = int(input())

A = [1,1]
for i in range(100):
    t = A[-1]
    tt = str(t)
    ttt = 0
    for i in tt:
        ttt += int(i)
    A.append(t+ttt)

print(A[N])