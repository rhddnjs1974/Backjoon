a,b,c = map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a == b:
    print(1000 + 100 * a)
elif b==c:
    print(1000+100*b)
elif a==c:
    print(1000+100*a)
else:
    print(max(a,b,c)*100)
