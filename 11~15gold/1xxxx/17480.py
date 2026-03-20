n = int(input())
m = 0
arr = list(input().split())
dic = {}
for i in range(0,2*n,2):
    dic[arr[i]]=int(arr[i+1])
    m += int(arr[i+1])

word = input()
canword = []

for i in range(len(word)-m+1):
    dic2 = dic.copy()
    for j in range(i,i+m):
        if (word[j] not in dic2) or dic2[word[j]]==0:
            break
        dic2[word[j]] -= 1
    
    

        if j==i+m-1:
            canword.append(word[i:i+m])

ans = set()

def making(word,start,end):
    if (end-start)<=2:
        ans.add(word)
        return
    
    if (end-start)%2==0:
        l = (end-start)//2
        
        x = word[start:start+l]
        y = word[start+l:end]

        making(word[:start]+x[::-1]+y+word[end:],start+l,end)
        making(word[:start]+x+y[::-1]+word[end:],start,start+l)
    else:
        l = (end-start)//2
        
        x = word[start:start+l]
        y = word[start+l:end]

        making(word[:start]+x[::-1]+y+word[end:],start+l,end)
        making(word[:start]+x+y[::-1]+word[end:],start,start+l)
        
        l = 1+((end-start)//2)
        
        x = word[start:start+l]
        y = word[start+l:end]

        making(word[:start]+x[::-1]+y+word[end:],start+l,end)
        making(word[:start]+x+y[::-1]+word[end:],start,start+l)

for i in canword:
    making(i,0,m)

print(len(ans))