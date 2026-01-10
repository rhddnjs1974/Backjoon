D = int(input())
d_digits = list(map(int, str(D)[::-1]))

best = -1
MAX_N = 12

for n in range(1, MAX_N + 1):
    if best !=-1 and 10 ** (n - 1) > best:
        break

    if n < len(d_digits):
        continue

    H = (n + 1) // 2 
    lo = 10 ** (H - 1)
    hi = 10 ** H

    d = d_digits + [0] * (n - len(d_digits))

    found_for_n = -1

    for prefix in range(lo, hi):
        s = str(prefix)
        high = [int(ch) for ch in s]

        a = [0] * n
        for i in range(H):
            a[n - 1 - i] = high[i]

        borrow = 0
        ok = True

        for k in range(0, n - H):
            b = a[n - 1 - k]
            ssum = d[k] + b + borrow
            a[k] = ssum % 10
            borrow = 1 if ssum >= 10 else 0

        for k in range(n - H, n):
            b = a[n - 1 - k]
            ssum = d[k] + b + borrow
            diff = ssum - a[k]
            if diff == 0:
                borrow = 0
            elif diff == 10:
                borrow = 1
            else:
                ok = False
                break

        if not ok or borrow != 0:
            continue

        if a[n - 1] == 0:
            continue

        x = 0
        for k in range(n - 1, -1, -1):
            x = x * 10 + a[k]

        found_for_n = x
        break

    if found_for_n != -1:
        if best == -1 or found_for_n < best:
            best = found_for_n

print(best)


