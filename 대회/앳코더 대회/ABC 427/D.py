import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N,M,K = map(int,input().split())
    S = input().rstrip()
    dp = [[0]*(N+1) for i in range(2*K+1)]
    for i in range(N):
        if S[i]=="A":
            dp[0][i+1] = 1
    
    graph = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int,input().split())
        graph[u].append(v)
        
    for x in range(1,2*K+1):
        for i in range(1,N+1):
            if x%2==0:
                f = 0
                for j in graph[i]:
                    if dp[x-1][j]==1:
                        f=1
                if f==1:
                    dp[x][i] = 1
            else:
                f = 1
                for j in graph[i]:
                    if dp[x-1][j]==0:
                        f=0
                if f==1:
                    dp[x][i] = 1
    
    if dp[2*K][1]==1:
        print("Alice")
    else:
        print("Bob")