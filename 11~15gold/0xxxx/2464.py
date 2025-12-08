n = int(input())
nn = n
x = 0
y = 0
arr = []
num = 0
if n%2==1:
    pr = 1
    nn &= ~(1<<0)
    num+=1
else:
    pr = 0
    
for i in range(1,1000):
    if 2**i>n*2:
        break
    if n & (1<<i):
        now = 1
        nn &= ~(1<<i)
        num+=1
    else:
        now = 0
    
    if x==0 and now==1 and pr==0:
        x = nn
        for j in range(num):
            x+= (1<<(i-1-j))

    if y==0 and now==0 and pr==1:
        y = nn + (1<<(i))
        for j in range(num-1):
            y+= (1<<j)
    pr = now
    
    
if x==y==0:
    print(0)
else:
    print(x,y)