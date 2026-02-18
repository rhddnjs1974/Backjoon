MOD = 1000000007

N = int(input())
S = list(map(int, input().split()))

if N < 3:
    print(0)
else:
    cnt = []
    sumlen = []
    for _ in range(N):
        cnt.append({})
        sumlen.append({})

    ans = 0

    for k in range(N):
        dk = cnt[k]
        lk = sumlen[k]

        for j in range(k):
            d = S[k] - S[j]

            dj = cnt[j]
            lj = sumlen[j]

            ext_cnt = 0
            ext_len = 0

            v = dj.get(d - 1)
            if v is not None:
                ext_cnt += v
                ext_len += lj[d - 1]

            v = dj.get(d)
            if v is not None:
                ext_cnt += v
                ext_len += lj[d]

            v = dj.get(d + 1)
            if v is not None:
                ext_cnt += v
                ext_len += lj[d + 1]

            ext_cnt %= MOD
            ext_len %= MOD

            if ext_cnt:
                new_cnt = ext_cnt
                new_len = (ext_len + ext_cnt) % MOD

                ans += new_len
                ans %= MOD

                prev = dk.get(d)
                if prev is None:
                    dk[d] = new_cnt
                    lk[d] = new_len
                else:
                    dk[d] = (prev + new_cnt) % MOD
                    lk[d] = (lk[d] + new_len) % MOD

            prev = dk.get(d)
            if prev is None:
                dk[d] = 1
                lk[d] = 2
            else:
                dk[d] = (prev + 1) % MOD
                lk[d] = (lk[d] + 2) % MOD

    print(ans % MOD)
