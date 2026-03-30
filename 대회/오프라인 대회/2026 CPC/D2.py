import sys
input = sys.stdin.readline

T = int(input())

def recursion(now):
    global pp,L,R,N
    pp=N-1
    while(True):
        if now+pp>R:
            next = now+pp
            break
        now += pp
        pp *= N
    
    pp = N-1
    while(True):
        if next -pp+(pp//N)<0:
            break####################
        next -= pp-(pp//N)

        if next<=R:
            break
        pp *= N
    

    pp //= (N-1)
    
    ma = pp*(N-1)+next
    ma = min(ma,R)
    
    p = (ma-next)//pp
    return next+p*pp

for test in range(T):
    L,R,N = map(int,input().split())
    
    ans = recursion(0)
    
    while(ans<L):
        ans = recursion(ans+1)

    print(ans)
        

    
