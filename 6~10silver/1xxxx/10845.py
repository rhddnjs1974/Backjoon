import sys
input = sys.stdin.readline

n = int(input())
q = []
head = 0
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if head < len(q):
            print(q[head])
            head += 1
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(q)-head)
    elif cmd[0] == "empty":
        if head == len(q):
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if head < len(q):
            print(q[head])
        else:
            print(-1)
    elif cmd[0] == "back":
        if head < len(q):
            print(q[-1])
        else:
            print(-1)
