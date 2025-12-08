import sys
input = sys.stdin.readline

n,d = map(int,input().split())
monst = []
equip = []
for i in range(n):
    a,x = map(int,input().split())
    if a==1:
        monst.append(x)
    else:
        equip.append(x)

monst.sort()
equip.sort()
equip.reverse()
l = len(equip)
ans = 0
for i in range(len(monst)):
    if d>monst[i]:
        d+=monst[i]
        ans+=1
    else:
        while(d<=monst[i] and equip):
            t = equip.pop()
            d *= t
        if d<=monst[i]:
            break
        d+= monst[i]
        ans+=1


print(ans+l)
        