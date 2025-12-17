n= int(input())
now = 1
s =1
e =1
ans =0
while(e<=n):
    if now==n:
        ans+=1
        now += (e+1-s)
        e+=1
        s+=1
    elif now<n:
        now += e+1
        e+=1
    else:
        now -= s
        s+=1

print(ans)