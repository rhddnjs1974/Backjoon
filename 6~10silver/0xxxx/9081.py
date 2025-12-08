for _ in range(int(input())):
    x = input()
    y = []
    for i in x:
        y.append(i)
    y = list(set(y))
    y.sort()
    z = [0]*len(x)
    for i in range(len(y)):
        for j in range(len(x)):
            if x[j]==y[i]:
                z[j] =i
                
    now = -1
    w=[]
    flag = 0
    for i in range(len(x)-1,-1,-1):
        if z[i]>=now:
            now = z[i]
            w.append(now)
        else:
            break
        if i==0:
            print(x)
            flag=1
            break
    if flag==1:
        continue


    mi = 100000000
    for j in range(i+1,len(x)):
        if mi>z[j]>z[i]:
            mi = z[j]
            J=j
    z[i],z[J] = z[J],z[i]
    zz = z[i+1:]
    zz.sort()
    for j in range(i+1,len(x)):
        z[j]=zz[j-i-1]
    
    ans = ""
    for i in z:
        ans+=y[i]
    print(ans)