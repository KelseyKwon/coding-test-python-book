"""
# 시도 1:  이렇게 했다가 실행 시간 초과 남. 원인 : 이중루프때문에. N이 엄청 커지면 매우 느려지므로 단일 루프로 한다. 누적합 방식!
# 각 스테이지에 도달한 사람수를 미리 계산한 후, 이를 기반으로 실패율 계산하기.
def solution(N, stages):
    failure = [0] * (N+1)
    failure[0] = 1
    rank = list(range(1, (N+1)))

    for i in range(1, (N+1)):
        try_stage = 0
        fail_stage = 0
        for j in range (len(stages)):
            if (stages[j] >= i):
                try_stage +=1
            if (stages[j] == i):
                fail_stage +=1
        if (try_stage == 0):
            failure[i] = 0
        else:
            failure[i] = fail_stage / try_stage
    
    sorted_rank = sorted(rank, key=lambda i : failure[i], reverse=True)
    return sorted_rank
"""

def solution(N, stages):
    # 각 스테이지에 도달한 사람 수를 저장할 배열
    count = [0] * (N + 2)  # N+2 크기로 만들어 마지막 스테이지(N+1)까지 포함

    # 각 스테이지에 도달한 사람 수 계산
    for stage in stages:
        count[stage] += 1

    # 총 시도한 사람 수
    total_players = len(stages)
    failure = []  # (스테이지 번호, 실패율)을 저장할 튜플플리스트

    for i in range(1, N + 1):
        if total_players == 0:  # 남은 플레이어가 없는 경우 실패율은 0
            failure.append((i, 0))
        else:
            fail_rate = count[i] / total_players
            failure.append((i, fail_rate))
            total_players -= count[i]  # 해당 스테이지에 도달한 사람 수를 제외

    # 실패율 기준으로 내림차순 정렬, 실패율이 같으면 스테이지 번호 기준 오름차순
    # -x[1]: 실패율(x[1])에 **음수 부호(-)**를 붙여 내림차순 정렬을 수행
    sorted_rank = [stage for stage, _ in sorted(failure, key=lambda x: (-x[1], x[0]))]
    return sorted_rank

# 저자 풀이
def solution(N, stages):
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1

    fails = {}
    total = len(stages)

    for i in range(1, N + 1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]

    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    return result


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # 반환값 : [3, 4, 2, 1, 5]
# print(solution(4, [4, 4, 4, 4, 4])) # 반환값 : [4, 1, 2, 3]

"""
note : 
초기에는 반복문을 돌면서 스테이지에 있는 플레이어들, 통과하지 못한 플레이어들을 직접 구했는데,
저자의 풀이는 스테이지별 도전자 수를 초기화하고 미리 지정해 놓아 N^2 시간복잡도를 더 줄일 수 있는 것.
스테이지별 단계 num과 실패율을 함께 저장해 나중에 실패율을 기준으로 단계 num을 정렬해야 하므로
두가지를 모두 저장할 수 있는 dictionary형 list가 적합하다.
"""
