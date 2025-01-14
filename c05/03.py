def solution(numbers):
    add_nums = []
    for i in range(len(numbers)):
        for j in range((i+1), len(numbers)):
            add_nums.append(numbers[i] + numbers[j])
    add_nums = sorted(set(add_nums))
    return add_nums

# 저자 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(set(answer))

#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
# print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]

"""
Note :
- numbers의 최대 데이터 개수는 100이므로 시간 복잡도는 고려하지 않아도 됨.
- 배열을 인덱스로 탐색할 때는 for i in range(len(numbers))을 사용하자!
- 시간 복잡도 : 모든 조합을 확인하는 과정에서 중복을 체크하는데 O(N^2), 그리고 이를 정렬하는데 log(N^2log(N^2))
"""