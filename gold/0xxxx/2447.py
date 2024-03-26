def star(n,a,b):
    if n==1:
        return

    m = n//3

    for i in range(m,2*m):
        for j in range(m,2*m):
            arr[a+i][b+j]=" "

    star(m,a,b)
    star(m,a+m,b)
    star(m,a+2*m,b)
    star(m, a, b+m)
    star(m, a + 2 * m, b+m)
    star(m, a, b+2*m)
    star(m, a + m, b+2*m)
    star(m, a + 2 * m, b+2*m)

N = int(input())

arr = [["*"]*N for i in range(N)]

star(N,0,0)

for i in arr:
    for j in i:
        print(j,end="")
    print()