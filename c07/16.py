# 내 풀이
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = list(map(lambda ps: (100 - ps[0]) // ps[1] if (100 - ps[0]) % ps[1] == 0 else (100 - ps[0]) // ps[1] + 1, zip(progresses, speeds)))

    queue = deque()
    queue.append(0)

    for i in range(1, len(days)):
        while queue and days[i] > days[queue.popleft()]:
            j = queue.popleft()
            answer.append(i-j)
            queue.clear()
        queue.append(i)

    # while queue:
    #     answer.append(len(days) - queue.popleft())
    #     queue.clear()

    if queue:
        answer.append(len(queue))

    return answer

#저자 풀이
import math

def solution(progresses, speeds):
  answer = [ ]
  n = len(progresses)
  # ➊ 각 작업의 배포 가능일 계산
  days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

  count = 0  # ➋ 배포될 작업의 수 카운트
  max_day = days_left[0]  # ➌ 현재 배포될 작업 중 가장 늦게 배포될 작업의 가능일

  for i in range(n):
    if days_left[i] <= max_day:  # ➍ 배포 가능일이 가장 늦은 배포일보다 빠르면
      count += 1
    else:  # ➎ 배포 예정일이 기준 배포일보다 느리면
      answer.append(count)
      count = 1
      max_day = days_left[i]

  answer.append(count)  # ➏ 마지막으로 카운트된 작업들을 함께 배포
  return answer
