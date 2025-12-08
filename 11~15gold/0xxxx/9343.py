import sys
input = sys.stdin.readline
########################################
c = 1000000007
sys.setrecursionlimit(10**5)
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

facto = [0]*4000001
facto[1] = 1
for i in range(2,4000001):
    facto[i] = (facto[i-1]*i)%c


t = int(input())
for i in range(t):
    k = int(input())
    n = 2*k

    A = facto[n] #분자
    B = facto[k]*facto[k+1] #분모

    ans = (A*power(B,c-2))%c

    print(ans)