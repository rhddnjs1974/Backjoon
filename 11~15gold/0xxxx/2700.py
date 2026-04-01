def on_segment(a,b,p):
    if ccw(*a,*b,*p)!=0:
        return 0
    if min(a[0],b[0]) < p[0] < max(a[0],b[0]) or min(a[1],b[1]) < p[1] < max(a[1],b[1]):
        return 1
    if p==a or p==b:
        return 1
    return 0

def inside(shape,dot):
    for i in range(len(shape)):
        if on_segment(shape[i-1],shape[i],dot)==1: #이걸 빼면 경계선 위에 있는 점도 내부점으로 판정
            return 0

    area1 = find_area(shape)
    area2 = 0

    for i in range(len(shape)):
        a = ccw(*shape[i-1],*shape[i],*dot)
        area2 += abs(a)

    if area1==area2:
        return 1
    else:
        return 0

def find_area(array): #넓이의 2배 return
    area = 0
    for i in range(1,len(array)-1):
        area += ccw(*array[0],*array[i],*array[i+1])
    return abs(area)

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)


P = int(input())
for _ in range(P):
    N = int(input())
    s = []
    for i in range(N):
        x,y = map(int,input().split())
        s.append((x,y))
    
    realans = []
    
    for i in range(30,-31,-1):
        ans = []
        for j in range(-30,31):
            if inside(s,(j,i)):
                ans.append(j)
        
        if len(ans)!=0:
            realans.append((i,ans[0],ans[-1]))
    
    print(len(realans))
    for x in realans:
        print(*x)