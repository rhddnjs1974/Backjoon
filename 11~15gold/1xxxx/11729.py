def move(N,fr,to):
    if N==0:return
    move(N-1,fr,6-fr-to)
    print(fr,to)
    move(N-1,6-fr-to,to)
N = int(input())
print(-1+2**N)
move(N,1,3)