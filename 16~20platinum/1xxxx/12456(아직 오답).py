import heapq

for T in range(int(input())):
    n, k = map(int,input().split())
    heap =[]
    for i in range(n):
        ci,ti,si = map(int,input().split()) #남은양, 유통기한, 만족도
        heapq.heappush(heap,(-ti,-si,ci)) #기한, 만족도, 양
    heapq.heappush(heap,(0,0,0))
    
    ans = 0
    
    t,s,c = heapq.heappop(heap)
    t = -t
    s = -s
    u= 0
    while(heap and t>0):
        
        if u==0:
            nowarr = c
            arr= [(s,c)]
        
        while(heap):
            pret,pres,prec = heapq.heappop(heap)
            pret = -pret
            pres = -pres
            if pret!=t:
                break
            nowarr+=prec
            arr.append((pres,prec))
            if nowarr>=t:
                break
        
        x = 0
        while(x<len(arr)):
            s,c = arr[x]
            p = min(t-pret,c)
            ans += min(t-pret,c)*s
            t -= p
            x+=1
            if t==pret:
                if c>p:
                    heapq.heappush(heap,(-pret,-s,c-p))
                break
        for i in range(x,len(arr)):
            s,c = arr[i]
            heapq.heappush(heap,(-pret,-s,c))
            
        t = pret
        s = pres
        u+=1
        
    print("Case #"+str(T+1)+":",ans)