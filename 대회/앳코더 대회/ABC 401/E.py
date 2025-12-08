import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []
for i in range(N+1):
    arr.append(set())
    
for _ in range(M):
    u,v = map(int,input().split())
    arr[u].add(v)
    arr[v].add(u)

s = set()

donthave = set()
for i in range(1,N+1):
    s = s.union(arr[i])
    
    print(i,s)
    if i==1:
        print(len(s))
    else:
        donthave.add(1)
        if i not in s:
            print(-1)
            donthave.add(i)
        else:
            flag = 0
            if len(donthave)!=0:
                dont = list(donthave)
                for j in dont:
                    if j not in s:
                        print(-1)
                        flag = 1
                    else:
                        donthave.remove(j)
            if flag==0:
                print(len(s)-i)