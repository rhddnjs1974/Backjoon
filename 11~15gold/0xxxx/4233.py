import sys
input = sys.stdin.readline
########################################
def power(a,b):
    global p
    if b==1:
        return a
    if b==0:
        return 1

    if b%2==0:
        return power(a,b//2)**2 % p
    else:
        return a*(power(a, b // 2) ** 2) % p


while(True):
    p,a = map(int,input().split())
    if p==a==0:
        break

    if power(a,p)==a:
        flag = 0
        for i in range(2, 1 + int(1 + p **0.5)):
            if p % i == 0:
                flag = 1
                break

        if flag == 0:
            print("no")
        else:
            print("yes")
    else:
        print("no")



