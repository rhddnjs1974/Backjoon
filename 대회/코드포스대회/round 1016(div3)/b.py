import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    x=0
    while(n%10==0):
        x+=1
        n = n//10
    
    n = str(n)
    ans = len(n)-1
    for i in n:
        if i=="0":
            x-=1
    
    print(ans+x)