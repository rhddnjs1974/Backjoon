import sys
input = sys.stdin.readline
import itertools

n = 1/(2**0.5)

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

arr = list(map(int,input().split()))

npr = itertools.permutations(arr,8)
ans = 0

for i in npr:

    arr2 = []
    arr2.append([0, i[0]])
    arr2.append([i[1]*n, i[1]*n])

    arr2.append([i[2], 0])
    arr2.append([i[3] * n, -i[3] * n])

    arr2.append([0, -i[4]])
    arr2.append([-i[5] * n, -i[5] * n])

    arr2.append([-i[6], 0])
    arr2.append([-i[7] * n, i[7] * n])
    p = 0
    for j in range(8):
        x = j
        y = (j+1)%8
        z = (j+2)%8
        t = ccw(*arr2[x],*arr2[y],*arr2[z])

        if t>0:
            p+=1
        else:
            p-=1
    if p==8 or p==-8:
        ans+=1

print(ans)