a,b,c = map(int,input().split())

x = 11*60*24+11*60+11

y = a*60*24+b*60+c

if y>=x:
    print(y-x)
else:
    print(-1)