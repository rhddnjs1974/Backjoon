import sys
import itertools
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    
    arr = list(input().rstrip().split())
    arr2 = []
    

    for i in range(n):
        t = ""
        b = 0
        for a in arr[i]:
            if 'A'<=a<='Z':
                b+=1
        x = sorted(arr[i].lower())
        y = ""
        for i in x:
            y+=i
        arr2.append(y+str(b))
    
    dic = {}
    for i in arr2:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    
    ans = 0

    for i in dic:
        ans += ( dic[i]*(dic[i]-1) ) // 2
    print(ans)