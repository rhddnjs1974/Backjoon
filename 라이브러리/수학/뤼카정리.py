n,k,p = map(int,input().split()) #p는 소수

binom = [[0]*(p+1) for i in range(p+1)]

for i in range(p+1):
    for j in range(i+1):
        if i==0 or j==0:
            binom[i][j] = 1
        else:
            binom[i][j] = (binom[i - 1][j] + binom[i - 1][j - 1]) % p

####### ^ pCp까지 전처리 #######

ans = 1
while (n!=0 and k!=0):
    ans = (ans * binom[(n % p)][(k % p)]) % p;  
    n //= p
    k //= p 

print(ans)