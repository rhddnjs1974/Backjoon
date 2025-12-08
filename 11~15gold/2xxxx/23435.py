n = int(input())
arr = []
for i in range(n):
    arr.append(i)

dic = {}
for i in range(n):
    dic[i] = [i]

while(True):
    arr2 = []
    now = []
    for i in range(len(arr)):
        now.append(arr[i])
        if len(now)==2:
            print("?",now[0],now[1],flush=True)
            wi = input()
            if wi=="<":
                arr2.append(now[0])
                dic[now[0]].append(now[1])
            else:
                arr2.append(now[1])
                dic[now[1]].append(now[0])
            now = []
    
    if now:
        arr2.append(now[0])
    
    arr = arr2
    if len(arr)<3:
        break

if len(arr)==2:
    print("?",arr[0],arr[1],flush=True)
    wi = input()
    if wi=="<":
        one = arr[0]
        dic[one].append(arr[1])
    else:
        one = arr[1]
        dic[one].append(arr[0])

    arr = []
    for i in dic[one]:
        if i == one:
            continue
        arr.append(i)
else:
    one = arr[0]
    arr = []
    for i in dic[one]:
        if i == one:
            continue
        arr.append(i)


while(True):
    arr2 = []
    now = []
    for i in range(len(arr)):
        now.append(arr[i])
        if len(now)==2:
            print("?",now[0],now[1],flush=True)
            wi = input()
            if wi=="<":
                arr2.append(now[0])
                dic[now[0]].append(now[1])
            else:
                arr2.append(now[1])
                dic[now[1]].append(now[0])
            now = []
    
    if now:
        arr2.append(now[0])
    
    arr = arr2
    if len(arr)<3:
        break

if len(arr)==2:
    print("?",arr[0],arr[1],flush=True)
    wi = input()
    if wi=="<":
        print("!",arr[0],flush=True)
    else:
        print("!",arr[1],flush=True)
else:
    print("!",arr[0],flush=True)