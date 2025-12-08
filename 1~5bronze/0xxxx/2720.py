t = int(input())
for _ in range(t):
    c = int(input())
    x = c//25
    c%=25
    y = c//10
    c%=10
    z = c//5
    c%=5
    print(x,y,z,c)