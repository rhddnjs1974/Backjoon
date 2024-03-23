import sys
input = sys.stdin.readline

def preorder(v):
    ans.append(v)
    for i in graph[v]:
        if i<0:
            continue
        preorder(i)

def inorder(v):
    i = graph[v][0]
    if i>=0:
        inorder(i)
    ans.append(v)
    i = graph[v][1]
    if i>=0:
        inorder(i)
def postorder(v):
    i = graph[v][0]
    if i >= 0:
        postorder(i)
    i = graph[v][1]
    if i >= 0:
        postorder(i)

    ans.append(v)


N = int(input())
graph = [[] for i in range(N)]
for i in range(N):
    a,b,c = input().split()
    x = ord(a)-65
    y = ord(b) - 65
    z = ord(c) - 65


    graph[x].append(y)
    graph[x].append(z)

ans = []
preorder(0)
for i in ans:
    print(chr(i+65),end="")
print()

ans = []
inorder(0)
for i in ans:
    print(chr(i+65),end="")
print()

ans = []
postorder(0)
for i in ans:
    print(chr(i+65),end="")