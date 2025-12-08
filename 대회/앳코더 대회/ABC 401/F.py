from collections import deque

# BFS로 트리의 깊이 구하기
def bfs(start, n, graph):
    dist = [-1] * (n + 1)  # 각 정점까지의 거리 배열
    dist[start] = 0
    q = deque([start])
    max_dist = 0
    farthest_node = start
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:  # 아직 방문하지 않았다면
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor
    
    return farthest_node, dist


N = int(input())

# 트리 그래프 초기화
graph = {i: [] for i in range(1, N + 1)}

# 간선 입력 받기
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 1번 정점에서 시작하여 가장 먼 노드를 찾고, 그 노드에서 다시 가장 먼 노드를 찾는 방식으로 지름 구하기
farthest_node1, dist1 = bfs(1, N, graph)
farthest_node2, dist2 = bfs(farthest_node1, N, graph)

# 가장 깊은 뿌리의 길이와 두 번째 깊은 뿌리의 길이 구하기
deepest_node = farthest_node1  # 가장 깊은 노드
second_deepest_node = farthest_node2  # 두 번째 깊은 노드

arr = []
for i in range(1, N + 1):
    if dist1[i] == max(dist1):  # 가장 깊은 뿌리에 있는 정점들
        arr.append(dist1[i] + max(dist2[1:])-1)  # 1번과의 거리 + 두 번째 깊은 뿌리의 길이
    else:
        arr.append(dist1[i] + max(dist2[1:])-1)  # 1번과의 거리 + 가장 깊은 뿌리의 길이

N = int(input())

# 트리 그래프 초기화
graph = {i: [] for i in range(1, N + 1)}

# 간선 입력 받기
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 1번 정점에서 시작하여 가장 먼 노드를 찾고, 그 노드에서 다시 가장 먼 노드를 찾는 방식으로 지름 구하기
farthest_node1, dist1 = bfs(1, N, graph)
farthest_node2, dist2 = bfs(farthest_node1, N, graph)

# 가장 깊은 뿌리의 길이와 두 번째 깊은 뿌리의 길이 구하기
deepest_node = farthest_node1  # 가장 깊은 노드
second_deepest_node = farthest_node2  # 두 번째 깊은 노드

arr2 = []
for i in range(1, N + 1):
    if dist1[i] == max(dist1):  # 가장 깊은 뿌리에 있는 정점들
        arr2.append(dist1[i] + max(dist2[1:])-1)  # 1번과의 거리 + 두 번째 깊은 뿌리의 길이
    else:
        arr2.append(dist1[i] + max(dist2[1:])-1)  # 1번과의 거리 + 가장 깊은 뿌리의 길이

print(arr)
print(arr2)

ans = 0
s = 0
for i in arr:
    s+=i

ans += s*len(arr2)
for i in arr2:
    ans +=(i+1)*len(arr)
print(ans)