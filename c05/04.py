# 내 풀이 (중간에 포기)
def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5]
        [2, 1, 2, 3, 2, 4, 2, 5]
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    answer_1 = patterns[0] * ((answers // len(patterns[0])) + 1)
    answer_2 = patterns[1] * ((answers // len(patterns[1])) + 1)
    answer_3 = patterns[2] * ((answers // len(patterns[2])) + 1)

    scores = [0, 0, 0]

    for i in range(len(answers)):
        if (answer_1[i] == answers[i]):
            scores[0] +=1
        if (answer_2[i] == answers[i]):
            scores[1] +=1
        if (answer_3[i] == answers[i]):
            scores[2] +=1

# 저자 풀이

def solution(answers):
  # ➊ 수포자들의 패턴
  patterns = [
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ] 
  # ➋ 수포자들의 점수를 저장할 리스트
  scores = [0] * 3    
  # ➌ 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      if answer == pattern[i % len(pattern)]:
        scores[j] += 1  
  # ➍ 가장 높은 점수 저장
  max_score = max(scores)
  # ➎ 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
  highest_scores = [ ]
  for i, score in enumerate(scores):
    if score == max_score:
      highest_scores.append(i + 1)
  return highest_scores
     
    
"""
note:
if answer == pattern[i % len(pattern)]:
 - 수포자의 반복되는 답안 패턴과 주어진 정답을 비교하여 일치 여부를 확인하는 핵십 로직
 - i : 현재 문제의 인덱스 (0에서 시작)
 - pattern : 수포자의 답안 패턴 리스트
 - len(pattern) : 해당 수포자의 패턴 길이
 - i % pattern : 현재 인덱스 i를 패턴 길이로 나눈 나머지를 계산한다. 
 - 이렇게 하면 인덱스가 패턴 길이를 넘더라도 패턴의 처음으로 도 ㄹ아가 반복할 수 있다.
    - 문제 번호가 0~4일때는 그대로 [0, 1, 2, 3, 4] 인덱스 사용
    - 문제 번호가 5~9일때는 나머지를 구해서 [0, 1, 2, 3, 4] 돌아감
 - answer == pattern[i % len(pattern)]
    - 현재 문제의 정답(answer)이 수포자의 반복 패턴에서 나온 답과 같은지 확인하는 조건.

코테에서 % 연산을 사용하는 응용 예시:
1. 주기적인 작업 수행
    리스트를 순회하며 매 3번쨰 요소마다 어떤 작업을 할때 ; if i%3 == 0을 활용하면 가능하다.
2. 순환 구조 구현
    리스트나 배열을 순환할 때 % 연산자를 사용하여 인덱스 계산 가능.
    인덱스가 리스트의 길이를 넘어설 경우 처음으로 되돌아가게 하는 데 유용
3. 날짜와 시간 계산
    날짜와 시간 계산에서 주기적인 패턴을 계산할 때
    월~일 요일 리스트가 있을 떄, 10일 후의 요일은 무엇인지 계산할 때 10 % 7하면 3번째 인덱스의 요일이 됨
4. 특정 조건에 맞는 요소 선택
    리스트에서 인덱스가 짝수/홀수 요소만 선택하거나 필터링할 때
"""
