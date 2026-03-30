import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def union(a,b):
    x = find(a)
    y = find(b)
    if x<y:
        parent[y] = x
        return y,x
    else:
        parent[x] = y
        return x,y
    
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


N, M = map(int,input().split())
capa = [0]+list(map(int,input().split()))
water = [0]+list(map(int,input().split()))

parent = [i for i in range(N+1)]

size = [1]*(N+1)
hongsu = [0]*(N+1)
ans = 0

for i in range(1,N+1):
    if capa[i]<water[i]:
        hongsu[i] = 1
        ans+=1

for query in range(M):
    w, *q = map(int,input().split())
    if w==1:
        x,y = q
        
        z,w = union(x,y)
        
        if z!=w:
            size[w]+=size[z]
            size[z] = 0
            
            capa[w] += capa[z]
            capa[z] = 0
            
            water[w] += water[z]
            water[z] = 0
            
            ans -= hongsu[w]
            ans -= hongsu[z]
            
            if capa[w]<water[w]:    
                ans+= size[w]
                hongsu[w] = size[w]
            else:
                hongsu[w] = 0
            
            hongsu[z] = 0
        
        
    else:
        
        print(ans)