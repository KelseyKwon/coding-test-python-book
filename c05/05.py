def solution(arr1, arr2):
    # multiply_result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    multiply_result = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(multiply_result)):
        for j in range(len(multiply_result[0])):
            for k in range(len(arr2)):
                multiply_result[i][j] += (arr1[i][k] * arr2[k][j])

    return multiply_result

# 저자 풀이
def solution(arr1, arr2):
  # ➊ 행렬 arr1과 arr2의 행과 열의 수
  r1, c1 = len(arr1), len(arr1[0])
  r2, c2 = len(arr2), len(arr2[0])
  
  # ➋ 결과를 저장할 2차원 리스트 초기화
  ret = [[0] * c2 for _ in range(r1)]

  # ➌ 첫 번째 행렬 arr1의 각 행과 두 번째 행렬 arr2의 각 열에 대해
  for i in range(r1):
    for j in range(c2):
      # ➍ 두 행렬의 데이터를 곱해 결과 리스트에 더해줌
      for k in range(c1):
        ret[i][j] += arr1[i][k] * arr2[k][j]
  return ret

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# arr1, arr2 = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
# print(solution(arr1, arr2)) # 반환값 : [[15, 15], [15, 15], [15, 15]]
#arr1, arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
#print(solution(arr1, arr2)) # 반환값 : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

"""
note :
- 2차원 배열에서 배열의 행의 길이를 가져올때는 len(배열), 열의 길이를 가져올때는 len(배열[0])
- for _ in range 구문 : 반복문 내에서 변수를 사용하지 않을 때 관례적으로 _ 사용
- 
"""

