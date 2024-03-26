P = [0]*101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
for i in range(5,101):
    P[i] = P[i-5]+P[i-1]

T = int(input())
for i in range(T):
    a = int(input())
    print(P[a])