def kanto(start,l):
    global s
    if l==1:
        return
    t = l//3
    for i in range(start+t,start+t+t):
        s[i]=" "

    kanto(start,t)
    kanto(start++2*t,t)

while(True):
    try:
        n = int(input())
        s = ["-"]*(3**n)
        kanto(0,(3**n))
        for i in s:
            print(i,end="")
        print()
    except:
        break