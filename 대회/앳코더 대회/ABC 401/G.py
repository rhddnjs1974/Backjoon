def solve():
    N, K = map(int, input().split())
    S = list(input().strip())

    # 각 문자가 가능한지 여부를 저장
    T = ['?'] * N
    
    # 'o'의 개수를 세고, 인접한 'o'가 없도록 처리
    current_o_count = 0
    
    # 먼저 'o'를 채우는 방식으로 처리
    for i in range(N):
        if S[i] == 'o':
            current_o_count += 1
            T[i] = 'o'
    
    # 'o'가 K개가 되어야 하므로, 남은 빈자리에 'o'를 배치
    for i in range(N):
        if S[i] == '?' and current_o_count < K:
            if i == 0 or T[i-1] != 'o':  # 인접한 'o'가 없으면 넣기
                T[i] = 'o'
                current_o_count += 1
    
    # 'o'가 K개가 되면, 나머지 '?'는 '.'으로 처리
    for i in range(N):
        if S[i] == '?' and current_o_count == K:
            T[i] = '.'
    
    # 결과 출력
    print("".join(T))

solve()