def solution(arr):
    arr.sort()
    return arr

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
# print(solution([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
# print(solution([1,6,7])) # 반환값 : [1, 6, 7]

"""
Note:
- sort() 메서드는 리스트 원본 자체의 값을 바꾸기 때문에 원본 리스트 그대로 두고 싶다면

def solution(arr):
    sorted_list - list(sort(arr))
    return sorted_list
와 같이 쓰면 된다.

- 입력크기가 10⁵일 때, O(NlogN)은 10⁵ X 16.61 이기 떄문에 O(NlogN)의 복잡도를 가지는 것은 괜찮다. O(N²)이 되는 정렬로 풀면 시간초과 나서 통과 못함
"""
