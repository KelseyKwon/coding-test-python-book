def solution(arr):
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    return unique_arr

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
# print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]

"""
Note:
- set()은 집합을 생성하는 내장함수이다.
- 집합은 중복값을 허용하지 않으므로 문제에서 요구하는 중복 문제를 한 번에 해결 가능
- 반복문을 통해 중복값을 확인해 제거하는 알고리즘은 시간복잡도가 O(N^2)으로 성능이 좋지 않다.
- set() 함수는 O(N) 보장.
- 배열의 길이가 1,000이라 짧은편이다.
"""