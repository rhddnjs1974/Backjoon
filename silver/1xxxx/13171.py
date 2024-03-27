import sys
input = sys.stdin.readline
########################################
def power(a,b):
    global c
    if b==1:
        return a
    if b==0:
        return 1

    if b%2==0:
        return power(a,b//2)**2 % c
    else:
        return a*(power(a, b // 2) ** 2) % c

a = int(input())
b = int(input())
c = 1000000007
print(power(a,b)%c)