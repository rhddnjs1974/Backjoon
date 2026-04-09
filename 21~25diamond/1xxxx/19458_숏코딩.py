n=int(input())
M=1000000007
a=[0]*(n+2)
p=1
for i in range(1,n+1):
 p=(p*2)%M
 a[i]=pow(p-1,M-2,M)
z=0
for i in range(2,n+1):
 z=(z+(i-1)*a[1])%M
 for j in range(1,n-i+2):
  a[j]=(a[j]-(i-1)*a[j+1])%M
print(z)