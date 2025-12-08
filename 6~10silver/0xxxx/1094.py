x = int(input())
s = 64
t=64

ans = 1

while(True):
    if s==x:
        break
    t = t//2
    if s-t>=x:
        s =s-t
    else:
        ans+=1
print(ans)