import sys
input = sys.stdin.readline
########################################
c = 7
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


a,b,cc = map(int,input().split())
k,l = map(int,input().split())

ans1 = power(a,power(b,cc))
ans3 = power(power(a,b),cc)

A = power(b,cc) #분자
B = a #분모

ans2 = (A*power(B,c-2))%c

if (ans3+k)%7==l and (ans2+k)%7==l:
    print(3)
elif (ans3+k)%7==l:
    print(1)
elif (ans2+k)%7==l:
    print(2)
else:
    print(0)