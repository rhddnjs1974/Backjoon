import sys
import math
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def update_lazy(node,start,end):
    if lazy[node] != 0:
        tree[node] += (number[end+1]-number[start])*lazy[node]
        if start!=end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def query(node, start, end, left, right):
    update_lazy(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query(node * 2, start, (start + end) // 2, left, right) + query(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)
def update_range(node, start, end, left, right, diff):
    update_lazy(node,start,end)
    if left>end or right<start:
        return
    if left<=start and end<=right:
        tree[node] += (number[end+1]-number[start])*diff
        if start!= end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return

    update_range(node*2,start,(start+end)//2,left,right,diff)
    update_range(node*2+1,(start+end)//2 +1,end,left,right,diff)
    tree[node] = tree[node*2] + tree[node*2 +1]

h = math.ceil(math.log2(200000))
tree_size = 1<<(h+1)
tree = [0]*tree_size
lazy = [0]*tree_size

n = int(input())
number = []
query1 = []
query2 = []

nq2 = 0
for i in range(n):
    x,*q = map(int,input().split())
    if x==1:
        query1.append(q)
    else:
        q.append(nq2)
        nq2+=1
        query2.append(q)
    
    number.append(q[0])
    number.append(q[1])

#print(query1)
#print(query2)
#print(number)

number = list(set(number))
ln = len(number)
for i in range(ln):
    number.append(number[i]+1)
    
number = list(set(number))
number.sort()


ln = len(number)+1

number.append(number[-1]+1) #****

dic = {}
for i in range(len(number)):
    dic[number[i]] = i

query2.sort(key=lambda x:x[2])


now = 0
ans = [0]*len(query2)
for i,j,k,nq2 in query2:
    while(now<k):

        a,b,c = query1[now]

        update_range(1, 0, ln-1, dic[a], dic[b], c)
        now+=1

    ans[nq2] = query(1, 0, ln-1, dic[i], dic[j])

for i in ans:
    print(i)