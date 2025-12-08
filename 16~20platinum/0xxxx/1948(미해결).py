import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    indegree[b] += 1
    
start,end = map(int,input().split())

q = [[0,start]]
dp = [[0,set()] for i in range(n+1)] #시간, 도로들


while(q):

    time,now = q.pop()
    for togo,t in graph[now]:
        indegree[togo] -= 1
        if dp[togo][0] < time+t:
            dp[togo][0] = time+t
            dp[togo][1] = set()
            dp[togo][1] = dp[now][1].union(dp[togo][1])
            dp[togo][1].add((now,togo))
        elif dp[togo][0] == time+t:
            dp[togo][1] = dp[now][1].union(dp[togo][1])
            dp[togo][1].add((now,togo))
            
        if indegree[togo]==0:
            q.append([dp[togo][0],togo])


print(dp[end][0])
print(len(dp[end][1]))

