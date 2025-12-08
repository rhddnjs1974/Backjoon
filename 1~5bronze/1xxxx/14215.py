a,b,c = map(int,input().split())

if max(a,b,c)*2>=a+b+c:
    print((a+b+c-max(a,b,c))*2-1)
else:
    print(a+b+c)