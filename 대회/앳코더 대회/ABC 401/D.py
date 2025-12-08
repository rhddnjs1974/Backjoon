import sys
input = sys.stdin.readline

N, K = map(int,input().split())
s = input().rstrip()


if N==1:
    if s=="?":
        if K==1:
            print("o")
        else:
            print(".")
    else:
        print(s)
else:
    arr = []
    numberq = []
    nownumberq = 0
    for i in range(N):
        if s[i]==".":
            arr.append(".")
            if nownumberq != 0:
                numberq.append(nownumberq)
                nownumberq = 0
        elif s[i]=="o":
            arr.append("o")
            if nownumberq != 0:
                numberq.append(nownumberq)
                nownumberq = 0
        else:
            if i==0:
                if s[1]=="o":
                    arr.append(".")
                    if nownumberq != 0:
                        numberq.append(nownumberq)
                        nownumberq = 0
                else:
                    arr.append("?")
                    nownumberq+=1
            elif i==N-1:
                if s[N-2]=="o":
                    arr.append(".")
                    if nownumberq != 0:
                        numberq.append(nownumberq)
                        nownumberq = 0
                else:
                    arr.append("?")
                    nownumberq+=1
            else:
                if s[i-1]=="o" or s[i+1]=="o":
                    arr.append(".")
                    if nownumberq != 0:
                        numberq.append(nownumberq)
                        nownumberq = 0
                else:
                    arr.append("?")
                    nownumberq+=1
    if nownumberq != 0:
        numberq.append(nownumberq)
        
    maxneedo = 0
    for x in numberq:
        maxneedo += (x+1)//2

    nownumbero = 0
    for i in arr:
        if i=="o":
            nownumbero += 1

    if maxneedo == K-nownumbero:
        now = 0
        i=0
        while(i<N):
            if arr[i]!="?":
                print(arr[i],end="")
                i+=1
            else:
                if numberq[now]%2==0:
                    while(i<N and arr[i]=="?"):
                        print("?",end="")
                        i+=1
                    now+=1
                else:
                    time = 0
                    while(i<N and arr[i]=="?"):
                        time +=1
                        if time%2==1:
                            print("o",end="")
                        else:
                            print(".",end="")
                        i+=1
                    now+=1
    elif K-nownumbero==0:
        for i in arr:
            if i=="o":
                print("o",end="")
            else:
                print(".",end="")
    else:
        for i in arr:
            print(i,end="")

