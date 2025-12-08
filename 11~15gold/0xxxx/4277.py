from fractions import Fraction

def parse_time(s):
    h, m, sec = map(int, s.split(':'))
    return h * 3600 + m * 60 + sec

while True:
    arr = input().strip()
    if arr == "-1":
        break

    t1s, t2s, t3s, t4s, t5s = arr.split()

    t1 = Fraction(parse_time(t1s))
    t2 = Fraction(parse_time(t2s))
    t3 = Fraction(parse_time(t3s))
    t4 = Fraction(parse_time(t4s))
    t5 = Fraction(parse_time(t5s))

    vA = Fraction(1, 1) / t3
    vC = ((t1 / t3) - 1) / (t1 - t4)
    vM = ((t2 / t3) - 1) / (t2 - t5)

    pC = 1 - vC * t4
    pM = 1 - vM * t5

    tCM = (pM - pC) / (vC - vM)

    total = int(tCM + Fraction(1, 2))

    h = (total // 3600) % 24
    total %= 3600
    m = total // 60
    s = total % 60

    print(f"{h:02d}:{m:02d}:{s:02d}")
