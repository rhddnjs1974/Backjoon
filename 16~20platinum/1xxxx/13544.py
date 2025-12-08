import sys
import bisect
import math
input = sys.stdin.readline

def merge(LEFT,RIGHT):
    sumarr = []
    i = 0
    j = 0
    while(i<len(LEFT) or j<len(RIGHT)):
        if i==len(LEFT):
            sumarr.append(RIGHT[j])
            j+=1
            continue
        elif j==len(RIGHT):
            sumarr.append(LEFT[i])
            i+=1
            continue
            
        if i==len(LEFT) and j==len(RIGHT):
            break
        
        if LEFT[i]<RIGHT[j]:
            sumarr.append(LEFT[i])
            i+=1
        else:
            sumarr.append(RIGHT[j])
            j+=1
    return sumarr

def Preprocessing(node,start,end):
    if start==end:

        tree[node].append(l[start])
        return
    Preprocessing(node*2,start,(start + end) // 2)
    Preprocessing(node*2 + 1 , (start + end) // 2 + 1, end)
    tree[node] = merge(tree[node*2], tree[node*2+1])
        
def query(node, start, end, left, right, K):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return len(tree[node])- bisect.bisect_left(tree[node],K+1)
        
    return query(node * 2, start, (start + end) // 2, left, right, K) + query(node * 2 + 1, (start + end) // 2 + 1, end, left, right, K)

n = int(input())
l = list(map(int,input().split()))
h = math.ceil(math.log2(n))
tree_size = 1<<(h+1)
tree = [[] for i in range(tree_size)]
m = int(input())

Preprocessing(1, 0, n - 1)
lastans = 0

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    i = a^lastans
    j = b^lastans
    k = c^lastans
    
    lastans = query(1,0,n-1,i-1,j-1,k)
    print(lastans)

