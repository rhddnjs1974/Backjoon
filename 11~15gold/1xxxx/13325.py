import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def countSubtreeNodes(currentNode):
    dp[currentNode] = 0
    for node in child[currentNode]:
        countSubtreeNodes(node)
        dp[currentNode] = max(dp[currentNode],(dp[node]+arr[node]))

    for node in child[currentNode]:
        ans[node] = dp[currentNode]-dp[node]

k = int(input())
n= 2**(k+1)
graph = [[] for i in range(n)]
child = [[] for i in range(n)]


dp = [0]*(n)
arr = [0,0]+list(map(int,input().split()))

ans = [0]*n

for i in range(1,2**k):
    child[i].append(i*2)
    child[i].append(1+i * 2)


countSubtreeNodes(1)

print(sum(ans))