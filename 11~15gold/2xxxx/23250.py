def move(N,K,fr,to):
    if N==1 and K==1:
        return (fr,to)
    c = (1<<(N-1))-1
    if K<=c:
        return move(N-1,K,fr,6-fr-to)
    elif (K==c+1):
        return (fr,to)
    else:
        return move(N-1,K-c-1,6-fr-to,to)
N,K=map(int,input().split())
print(*move(N,K,1,3))