n = int(input())
ans = n
i=1
t=1
while(True):
    p = ((n-1)//i )
    if p==0:
        break
    q = (n-1)//p
    ans += (q-i+1)*p
    i = q+1
    if i>n-1:
        break

    
print(ans)