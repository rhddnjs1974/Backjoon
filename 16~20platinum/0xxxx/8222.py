import sys
input = sys.stdin.readline

# -------- SPF & Omega(Ω) 전처리 --------

def build_spf_and_omega(max_a):
    """0..max_a 에 대해 최소 소인수(spf)와 Ω(x)를 미리 계산"""
    spf = [0] * (max_a + 1)
    # 에라토스테네스로 SPF 구하기
    limit = int(max_a ** 0.5)
    for i in range(2, limit + 1):
        if spf[i] == 0:               # i가 소수
            for j in range(i * i, max_a + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    for i in range(2, max_a + 1):
        if spf[i] == 0:
            spf[i] = i                # 자기 자신이 최소 소인수 (소수)

    # Ω(x) 계산: Ω(1) = 0, Ω(x) = 1 + Ω(x / spf[x])
    omega = [0] * (max_a + 1)
    for x in range(2, max_a + 1):
        omega[x] = omega[x // spf[x]] + 1

    return spf, omega


# -------- 한 수의 약수 구하기 (spf 이용) --------

def get_divisors_single(v, spf):
    """spf를 이용해 v의 모든 약수 리스트를 반환"""
    if v == 1:
        return [1]
    fac = []
    x = v
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        fac.append((p, cnt))

    divs = [1]
    for p, e in fac:
        cur_len = len(divs)
        mul = 1
        for _ in range(e):
            mul *= p
            for i in range(cur_len):
                divs.append(divs[i] * mul)
    return divs


# -------- 메인 로직 --------

def main():
    n = int(input().strip())
    a = [int(input().strip()) for _ in range(n)]

    max_a = max(a)
    spf, omega = build_spf_and_omega(max_a)

    # 각 인덱스의 Ω(a[i]) 미리 저장
    w = [omega[val] for val in a]

    # 값 v -> 약수 리스트 캐시 (같은 값 여러 번 안 팩터라이즈하게)
    div_cache = {}

    def get_divs(v):
        if v in div_cache:
            return div_cache[v]
        dv = get_divisors_single(v, spf)
        div_cache[v] = dv
        return dv

    # best1[g], best2[g] : g의 배수인 수들 중
    #   - best1[g] : Ω(a[j]) 최소인 인덱스 j
    #   - best2[g] : 그 다음으로 좋은 인덱스
    # 파이썬에서는 -1을 "없음" 상태로 쓰자.
    best1 = [-1] * (max_a + 1)
    best2 = [-1] * (max_a + 1)

    # -------- 전처리: 각 약수 g에 대해 best1, best2 채우기 --------
    for idx, val in enumerate(a):
        divs = get_divs(val)
        wi = w[idx]
        for g in divs:
            b1 = best1[g]
            if b1 == -1:
                # 아직 아무도 없으면 바로 1등
                best1[g] = idx
            else:
                # Ω 비교 + 인덱스 tie-break
                if wi < w[b1] or (wi == w[b1] and idx < b1):
                    # 지금 idx가 더 좋으면 1등으로, 기존 1등을 2등으로
                    best2[g] = b1
                    best1[g] = idx
                else:
                    b2 = best2[g]
                    if b2 == -1 or wi < w[b2] or (wi == w[b2] and idx < b2):
                        best2[g] = idx

    # -------- 각 i에 대해 답 찾기 --------
    INF = 10**18
    out = []

    for i, val in enumerate(a):
        best_cost = INF
        best_j = -1
        wi = w[i]
        divs = get_divs(val)

        for g in divs:
            j = best1[g]
            if j == i:
                j = best2[g]
            if j == -1:
                continue

            # d(a_i, a_j) = Ω(ai) + Ω(aj) - 2Ω(g)
            cost = wi + w[j] - 2 * omega[g]

            if cost < best_cost or (cost == best_cost and (best_j == -1 or j < best_j)):
                best_cost = cost
                best_j = j

        # 문제는 1-based index 요구
        out.append(str(best_j + 1))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
