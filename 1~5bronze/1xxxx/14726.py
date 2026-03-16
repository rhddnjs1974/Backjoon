for test in range(int(input())):
    n = input()
    now = 0
    f=0
    for i in n:
        i = int(i)
        f+=1
        if f%2==1:
            i *= 2
        if i>=10:
            i-=9
        now += i
    
    if now%10==0:
        print("T")
    else:
        print("F")