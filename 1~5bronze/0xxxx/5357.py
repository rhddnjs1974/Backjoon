for _ in range(int(input())):
    a= input()
    b = [0]
    for i in a:
        if i != b[-1]:
            b.append(i)
    for i in b[1:]:
        print(i,end="")
    print()