while(True):
    mo = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    a = input()
    if a=="#":
        break
    ans=0
    for i in a:
        if i in mo:
            ans+=1
    print(ans)