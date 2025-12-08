import sys
input = sys.stdin.readline

def make_pi(pattern):
    l = len(pattern)
    arr = [0 for _ in range(l)]

    pidx = 0
    for idx in range(1, l):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = arr[pidx - 1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            arr[idx] = pidx

    return arr

def KMP(word, pattern):
    pi_table = make_pi(pattern)

    results = []
    pidx = 0

    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = pi_table[pidx - 1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx - len(pattern) + 2)
                pidx = pi_table[pidx]
            else:
                pidx += 1
    return results

F = ["0","1"]
for i in range(26):
    F.append(F[i+1]+F[i])
#F[25] 길이 > 100,000

T=0
while(True):
    T +=1
    try:
        n = int(input())
    except:
        break
    try:
        p = input().rstrip()
    except:
        break
    if p=="":
        break
    l = len(p)

    dp=[0,0]
    if p=="0":
        dp[0] = 1
    if p=="1":
        dp[1] = 1


    for i in range(n-1):
        dp.append(dp[i]+dp[i+1])
        if l!=1:
            if i>26:
                if i%2==0:
                    A = F[27][-l + 1:] + F[26][:l - 1]
                else:
                    A = F[26][-l + 1:] + F[27][:l - 1]
            else:
                A = F[i+1][-l+1:] + F[i][:l-1]
            k = KMP(A,p)

            dp[i+2]+=len(k)

    print("Case %d: %d"%(T,dp[n]))
