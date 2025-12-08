A,B,V = map(int,input().split())

now = A

if now>=V:
    print(1)
else:
    x = V-now
    print(int(2+((x-0.1)//(A-B))))