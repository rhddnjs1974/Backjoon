while(True):
    a=int(input())
    if a==0:break
    b=0
    for i in range(a+1):
        b+=i
    print(b)