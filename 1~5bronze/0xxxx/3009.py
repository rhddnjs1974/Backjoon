
a,b = map(int,input().split())
aa,bb= map(int,input().split())
aaa,bbb= map(int,input().split())

if a==aa:
    x = aaa
elif a==aaa:
    x=aa
else:
    x=a

if b==bb:
    y=bbb
elif b==bbb:
    y=bb
else:
    y=b
print(x,y)