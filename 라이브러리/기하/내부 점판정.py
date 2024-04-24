def inside(shape,dot):
    area1 = find_area(shape)
    area2 = 0

    for i in range(len(shape)):
        a = ccw(*shape[i-1],*shape[i],*dot)
        area2 += abs(a/2)

    if area1==area2:
        return 1
    else:
        return 0

def find_area(array):
    area = 0
    for i in range(1, len(array)-1):
        area += ccw(*array[0], *array[i], *array[i + 1])
    area = abs(area)
    return area*0.5

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c
