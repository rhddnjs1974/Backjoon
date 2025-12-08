for i in range(3):
    a,b,c,d,e,f = map(int,input().split())
    t1 = a*3600+b*60+c
    t2 = d*3600+e*60+f
    t = t2-t1
    h = t//3600
    t %= 3600
    m = t//60
    t %= 60
    print(h,m,t)
