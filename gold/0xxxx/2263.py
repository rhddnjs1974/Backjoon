import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

index = [0]*(n+1)
for i in range(n):
    index[inorder[i]] = i
ans=[]

def preorder(ins,ine,pos,poe):
    if ins>ine or pos>poe:
        return
    root = postorder[poe]

    ans.append(root)



    point = index[root]


    preorder(ins,point-1,pos,point-ins+pos-1)
    preorder(point+1,ine,point-ins+pos,poe-1)



preorder(0,n-1,0,n-1)
print(*ans)