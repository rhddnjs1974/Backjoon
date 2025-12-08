

for T in range(int(input())):
    n, k = map(int,input().split())
    arr =[]
    for i in range(n):
        ci,ti,si = map(int,input().split()) #남은양, 유통기한, 만족도
        arr.append((ci,ti,si))
    arr.sort(key=lambda x:-x[2])
    now = 0
    ans = 0
    for a,b,c in arr:
        if b<=now:
            continue
        x = min(a,b-now)
        ans += (x*c)
        now += x
    
    print("Case #"+str(T+1)+":",ans)