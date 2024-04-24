import sys
input = sys.stdin.readline

def find_area(array):
    area = 0
    for i in range(1, len(array)-1):
        area += ccw(*array[0], *array[i], *array[i + 1])
    area = abs(area)
    return area*0.5

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

N = int(input())
arr= []
for i in range(N):
    arr.append(list(map(int,input().split())))

ans = find_area(arr)
print("%.1f"%(abs(ans)))