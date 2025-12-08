for _ in range(int(input())):
    l,r,s = map(int,input().split())
    if r-s<=s-l:
        print(2*r-2*s)
    else:
        print(2*s-2*l+1)