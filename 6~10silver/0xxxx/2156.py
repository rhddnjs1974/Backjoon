n = int(input())
arr= []
for i in range(n):
    arr.append(int(input()))

dp_0 = [0]*(n+1)
dp_1 = [0]*(n+1)
dp_2 = [0]*(n+1)

dp_1[1] = arr[0]

for i in range(1,n):
    dp_0[i+1] = max(dp_2[i],dp_1[i],dp_0[i])
    dp_1[i+1] = max(dp_1[i-1],dp_2[i-1],dp_0[i]) + arr[i]
    dp_2[i+1] = dp_1[i] + arr[i]

print(max(max(dp_1),max(dp_2),max(dp_0)))
