for _ in range(3):
    n = int(input())
    x = 0
    for i in range(n):
        x+=int(input())
    if x==0:
        print(0)
    elif x>0:
        print("+")
    else:
        print("-")