a,b,c = map(int,input().split())
ans = (a-2015)*4
x = b*100 + c
if x<230:
    ans+=1
elif x<532:
    ans+=2
elif x<832:
    ans+=3
elif x<1131:
    ans+=4
else:
    ans+=5
print(ans)