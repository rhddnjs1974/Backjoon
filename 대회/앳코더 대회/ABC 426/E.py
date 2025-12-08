import sys
input = sys.stdin.readline

def Axt(t):
    global tsx, tsy, tgx, tgy,asx, asy, agx, agy,vtx,vty,vax,vay
    
    return tsx-asx + (vtx-vax)*t
def Ayt(t):
    global tsx, tsy, tgx, tgy,asx, asy, agx, agy,vtx,vty,vax,vay
    
    return tsy-asy + (vty-vay)*t

def Aft(t):
    return Axt(t)**2 + Ayt(t)**2

def Bft(t):
    global tsx, tsy, tgx, tgy,asx, asy, agx, agy,vtx,vty,vax,vay
    
    return (tgx-asx-vax*t)**2 + (tgy-asy-vay*t)**2

def Cft(t):
    global tsx, tsy, tgx, tgy,asx, asy, agx, agy,vtx,vty,vax,vay
    
    return (tsx-agx+vtx*t)**2 + (tsy-agy+vty*t)**2


T = int(input())
for _ in range(T):
    tsx, tsy, tgx, tgy = map(int,input().split())
    asx, asy, agx, agy = map(int,input().split())
    
    ans = 1e9
    
    LT = ( (tgx-tsx)**2 + (tgy-tsy)**2 )**0.5
    LA = ( (agx-asx)**2 + (agy-asy)**2 )**0.5
    
    vtx = (tgx-tsx)/LT
    vty = (tgy-tsy)/LT
    vax = (agx-asx)/LA
    vay = (agy-asy)/LA
    
    t1 = min(LT,LA)
    t2 = max(LT,LA)
    
    if ( (vtx-vax)**2 + (vty-vay)**2 )!=0:
        tta = - ( (tsx-asx)*(vtx-vax) + (tsy-asy)*(vty-vay) ) / ( (vtx-vax)**2 + (vty-vay)**2 )
        if tta<0:
            tta=0
        if tta>t1:
            tta=t1
    else:
        tta = 0
    ans = min(ans,Aft(0),Aft(t1),Aft(tta))


    
    if LT<LA:
        ttb = ( (tgx-asx)*vax + (tgy-asy)*vay )/(vax**2  + vay**2 )
        ans = min(ans,Bft(t1),Bft(t2),Bft(ttb))
    else:
        ttc = -( (tsx-agx)*vtx + (tsy-agy)*vty  ) / (vtx**2 + vty**2 )
        ans = min(ans,Cft(t1),Cft(t2),Cft(ttc))
    
    last = (tgx-agx)**2 + (tgy-agy)**2
    ans = min(ans,last)
    
    print(ans**0.5)