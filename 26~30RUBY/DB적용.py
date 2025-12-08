import random
arr = [[0]*14 for i in range(8)]

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
def dfs(x,y,i,l,t):
    if i==l:
        return 1
    xxx = 0
    for d in range(8):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx<0 or nx>=8 or ny<0 or ny>=14:
            continue
        if arr[nx][ny]==t[i]:
            xxx = max(xxx,dfs(nx,ny,i+1,l,t))
            if xxx==1:
                break

    return xxx

def test(n):
    q = str(n)
    
    t = []
    for i in q:
        t.append(int(i))
    
    flag=0
    for i in range(8):
        for j in range(14):
            if arr[i][j]==t[0]:
                if dfs(i,j,1,len(t),t)==1:
                    flag=1
                    break
        if flag==1:
            break
    return flag

###################################################위는 체크용 함수

now = '8275981204568249508201534365612142678901790234567890174453456139012302567890126456802012345778915292012315391921'

for i in range(8):
    for j in range(14):
        arr[i][j] = int(now[i*14+j])


# ====== 하이브리드 힐클라임 + DB(60) 관리 루프 ======

# 점수 정의: first_fail - 1
MAXCHECK = 8141  # 네 코드 상한 그대로 유지

def first_fail():
    for case in range(1, MAXCHECK):
        if test(case) == 0:
            return case
    return MAXCHECK  # 상한 내에서는 모두 읽힘

def score_of_arr():
    return first_fail() - 1

def serialize_arr():
    # 8줄*14자리 문자열
    return ''.join(str(arr[i][j]) for i in range(8) for j in range(14))

def deserialize_to_arr(s):
    # s 길이 112 고정 가정
    for i in range(8):
        for j in range(14):
            arr[i][j] = int(s[i*14 + j])

# ---- 초기 상태 평가
cur_first_fail = first_fail()
cur_score = cur_first_fail - 1
best_first_fail = cur_first_fail
best_score = cur_score
best_snapshot = serialize_arr()

prev_first_fail = cur_first_fail   # ← 추가: '직전 스텝' 기준

# ---- DB 구조: (score, snapshot_string), 점수 내림차순, 점수는 모두 달라야 함
DB = []
def db_sorted_insert_or_replace(score, snap):
    """규칙:
       - 점수는 모두 달라야 함 (동일 점수 존재 시 그 데이터를 '대체')
       - 내림차순 유지
       - 크기 60 유지: 가득차 있고 새로운 점수가 최솟값 k 미만이면 무시,
                       k 이상이면 삽입하고 k 점수 항목 제거
    """
    global DB
    # 동일 점수 존재여부
    same_idx = next((i for i,(sc,_) in enumerate(DB) if sc == score), None)

    if len(DB) < 60:
        # 자리 남으면 동일 점수면 대체, 아니면 추가
        if same_idx is not None:
            DB[same_idx] = (score, snap)
        else:
            DB.append((score, snap))
        # 내림차순 정렬
        DB.sort(key=lambda x: x[0], reverse=True)
        return

    # 가득 찬 경우
    k = min(DB, key=lambda x: x[0])[0]  # 최솟값
    if score < k:
        # 1) 현재 데이터 점수가 k 미만이면 갱신 안 함
        return
    if same_idx is not None:
        # 2) 같은 점수 존재 시 그 데이터 대체
        DB[same_idx] = (score, snap)
        DB.sort(key=lambda x: x[0], reverse=True)
        return
    # 3) 같은 점수 없으면 추가 + 최솟값 제거
    DB.append((score, snap))
    # 정렬 후 꼴찌 제거(최솟값 k 하나 제거)
    DB.sort(key=lambda x: x[0], reverse=True)
    DB.pop()  # 가장 낮은 점수 제거 (유일성 보장)

# DB 시작: 현재 보드를 등록
db_sorted_insert_or_replace(cur_score, serialize_arr())

# ---- 탐색 파라미터
patience = 12                 # 정체 허용 횟수(네 노트의 15/18/12 가변값)
steps_since_best = 0          # 최고 점수 갱신 이후 경과 스텝 수
db_updates_since_best = 0     # 최고 점수 갱신 이후 DB 갱신 횟수

# DB를 여러 번 갱신해도 최고 점수가 갱신되지 않을 때 리주입 트리거
REINJECT_AFTER_DB_UPDATES = 5

# 전체 탐색 예산(무한 루프 방지용, 필요 없으면 크게 올려도 됨)
TOTAL_STEPS_BUDGET = 20000

for step in range(TOTAL_STEPS_BUDGET):
    # --- 단일 칸 변경 중 최선(상승) 혹은 유지(동률) 선택 ---
    # 현재 first_fail / score
    base_first_fail = first_fail()
    base_score = base_first_fail - 1

    best_move = None          # (gain_first_fail, i, j, new_digit)
    best_eq_move = None       # (same_first_fail, i, j, new_digit)

    # 모든 칸/숫자 후보 검사
    for i in range(8):
        if i==4:
            print("계산 절반")
        for j in range(14):
            original = arr[i][j]
            for k in range(10):
                if k == original:
                    continue
                arr[i][j] = k
                ff = first_fail()
                # 상승 후보
                if ff > base_first_fail:
                    if (best_move is None) or (ff > best_move[0]):
                        best_move = (ff, i, j, k)
                # 유지 후보(동점)
                elif ff == base_first_fail:
                    if best_eq_move is None:
                        best_eq_move = (ff, i, j, k)
                # 롤백
                arr[i][j] = original

    # 규칙 1: 상승 가능하면 그 중 최댓값을 채택
    if best_move is not None:
        _, ii, jj, kk = best_move
        arr[ii][jj] = kk
    # 규칙 2: 상승 후보 없으면 유지되는 것 중 하나 선택
    elif best_eq_move is not None:
        _, ii, jj, kk = best_eq_move
        arr[ii][jj] = kk
    else:
        # 어떤 단일 변경도 유지조차 못하면 무작위 한 칸을 변경(드문 케이스)
        ii = random.randrange(0, 8)
        jj = random.randrange(0, 14)
        curv = arr[ii][jj]
        kk = (curv + 1 + random.randrange(0, 9)) % 10
        arr[ii][jj] = kk

    # --- 적용 후 평가 ---
    cur_first_fail = first_fail()
    cur_score = cur_first_fail - 1

    # (A) 직전 스텝 대비 상승 중이면 정체 카운터 리셋
    if cur_first_fail > prev_first_fail:
        steps_since_best = 0
    else:
        steps_since_best += 1
    prev_first_fail = cur_first_fail  # 직전 값 업데이트

    # (B) 역대 최고치 갱신이면 best 갱신 + 보조 카운터/인내도 조정
    if cur_first_fail > best_first_fail:
        best_first_fail = cur_first_fail
        best_score = cur_score
        best_snapshot = serialize_arr()
        steps_since_best = 0
        db_updates_since_best = 0
        patience = 12

    # --- 정체 시 처리: DB 갱신 + 두 칸 랜덤 변경 ---
    if steps_since_best >= patience:
        # DB 갱신 (현재 점수/스냅샷으로)
        db_sorted_insert_or_replace(cur_score, serialize_arr())
        db_updates_since_best += 1

        # 임의의 두 칸을 임의의 숫자로 바꾼다
        for _ in range(2):
            x = random.randrange(0, 8)
            y = random.randrange(0, 14)
            arr[x][y] = random.randrange(0, 10)

        # 리셋
        steps_since_best = 0
        patience = 12

        # DB 여러 번 갱신해도 최고 점수 갱신이 없으면 DB에서 무작위 리주입
        if db_updates_since_best >= REINJECT_AFTER_DB_UPDATES and len(DB) > 0:
            sc, snap = random.choice(DB)
            deserialize_to_arr(snap)
            best_first_fail = sc + 1  # 점수 -> first_fail 환산
            best_score = sc
            best_snapshot = snap
            steps_since_best = 0
            db_updates_since_best = 0
            patience = 12
    
    print(best_score,"best_score")
    print(step,"step")
    print(arr)
    print(steps_since_best,"steps_since_best")
    print(DB)
    print(cur_score,"cur_score")

# ---- 탐색 종료: 최고 스냅샷으로 복원 후 출력 ----
deserialize_to_arr(best_snapshot)

# 8줄 × 14자리 출력
for i in range(8):
    line = ''.join(str(arr[i][j]) for j in range(14))
    print(line)
print("first_fail:", best_first_fail)
print("score:", best_score)
