x, p = map(float,input().split())
if p==0:
    print(0.0000)
    exit()
x /=100
p /=100

def P0(A,B):
    global p,x
    ja = 1-((1-p)/p)**(A)
    mo = 1-((1-p)/p)**(A+B)
    return ja/mo
    
def Ex(A,B):
    global x
    return B*P0(A,B) - A*(1-P0(A,B))*(1-x)

B=1
A = 0
ans=0.0000
while(B<100000):
    jun = Ex(1,B)
    for i in range(2,1000000):
        now = Ex(i,B)

        if now>jun-0.00001:
            jun = max(jun,now)
            continue
        else:
            break
    if A<=i:
        A=i
    else:
        break
    ans = max(ans,jun)
    B+=1
print(ans)