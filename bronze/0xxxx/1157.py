arr = [0]*26
n = input()
n = n.lower()
for i in n:
    arr[ord(i)-97]+=1

ma = max(arr)
ans = -2
for i in range(26):
    if arr[i]==ma:
        if ans==-2:
            ans = i
        else:
            ans = -1
            break



if ans==-1:
    print("?")
else:
    print(chr(ans+65))