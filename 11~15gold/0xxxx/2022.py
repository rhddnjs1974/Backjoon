x,y,c = map(float,input().split())

def cal(x,y,w):
    ja = (x**2 -w**2)**0.5
    ja2 = (y**2 - w**2)**0.5
    rja = ja*ja2
    rmo = ja + ja2
    return rja/rmo

mi = 0
ma = min(x,y)
while(mi+0.0001<ma):
    
    mid = (mi+ma)/2
    a = cal(x,y,mid)

    if a<c:
        ma = mid
    else:
        mi = mid

print(mid)