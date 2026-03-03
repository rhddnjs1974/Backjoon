import sys
input = sys.stdin.readline

arr1 = [0, 0]
arr2 = [0, 0]
arr3 = [0, 0]

def newnode():
    arr1.append(0)
    arr2.append(0)
    arr3.append(0)
    return len(arr3)-1

def add(v, d):
    node = 1
    arr3[node] += d
    
    for b in range(30, -1, -1):
        if ((v >> b) & 1) == 0:
            nx = arr1[node]
            if nx == 0:
                nx = newnode()
                arr1[node] = nx
            node = nx
        else:
            nx = arr2[node]
            if nx == 0:
                nx = newnode()
                arr2[node] = nx
            node = nx
        arr3[node] += d

def kthlargest(x, k):
    node = 1
    res = 0
    for b in range(30, -1, -1):
        xb = (x >> b) & 1
        pp = xb ^ 1
        if pp == 0:
            p = arr1[node]
        else:
            p = arr2[node]
        cp = 0
        if p != 0:
            cp = arr3[p]
        if cp >= k:
            res |= (1 << b)
            node = p
        else:
            k -= cp
            if xb == 0:
                node = arr1[node]
            else:
                node = arr2[node]
    return res

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for v in A:
    add(v, 1)

for _ in range(Q):
    t, i, x = map(int, input().split())
    if t == 1:
        i -= 1
        add(A[i], -1)
        A[i] = x
        add(A[i], 1)
    else:
        print(kthlargest(x, i))