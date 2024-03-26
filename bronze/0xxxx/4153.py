while(True):
    a,b,c= map(int,input().split())
    if a==b==c==0:
        break
    x = [a,b,c]
    x.sort()
    if (x[0]**2)+(x[1]**2)==x[2]**2:
        print("right")
    else:
        print("wrong")