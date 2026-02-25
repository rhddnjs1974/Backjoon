A,B,C,N = map(int,input().split())

flag = 0

for i in range(301):
    for j in range(301):
        if ( N - A*i - B*j )<0:
            continue
        
        if ( N - A*i - B*j ) % C == 0:
            flag=1

print(flag)