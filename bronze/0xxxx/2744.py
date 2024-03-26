a = input()
for i in a:
    if i.islower():
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")