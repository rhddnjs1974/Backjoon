import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(0)
    elif x > 0:
        p = 1   
        while p < x:
            p *= 2
            
        print((4 * p)+x-4)
    else:
        p = 1
        while p < -x:
            p *= 2
        print((6 * p)-x-4)