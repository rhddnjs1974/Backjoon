import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def countSubtreeNodes(currentNode):
    dp[currentNode] = 0
    for node in child[currentNode]:
        countSubtreeNodes(node)

    array =[]
    for node in child[currentNode]:
        array.append(dp[node])
    array.sort()

    for i in range(len(array)):
        dp[currentNode] = max(dp[currentNode],array[i]+len(child[currentNode])-i)


n = int(input())
child = [[] for i in range(n)]

arr = list(map(int,input().split()))

for i in range(n):
    p = arr[i]
    if p!=-1:
        child[p].append(i)

dp = [1e9]*(n)

countSubtreeNodes(0)

print(dp[0])