T = int(input())

for i in range(T):
    h,w,n = map(int,input().split())
    a = n%h
    if a==0:
        a = h
    b = 1+(n-1)//h
    print(a*100+b)