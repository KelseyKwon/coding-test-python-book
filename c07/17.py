from collections import deque

def solution(cards1, cards2, goal):
    answer = ''

    queue_card1 = deque(cards1)
    queue_card2 = deque(cards2)
    queue_goal = deque(goal)

    N = len(queue_goal)

    for _ in range(N):
        if queue_card1 and queue_goal[0] == queue_card1[0]:
            queue_goal.popleft()
            queue_card1.popleft()
        elif queue_card2 and queue_goal[0] == queue_card2[0]:
            queue_goal.popleft()
            queue_card2.popleft()
        else:
            answer = 'No'
    
    if (len(queue_goal) == 0):
        answer = "Yes"
    else:
        answer = 'No'

    return answer

# 저자 풀이
from collections import deque

def solution(cards1, cards2, goal):
  # cards와 goal을 deque로 변환
  cards1 = deque(cards1)
  cards2 = deque(cards2)
  goal = deque(goal)

  # ➊ goal의 문자열을 순차적으로 순회
  while goal:
    if cards1 and cards1[0] == goal[0]:  # ➋ card1의 front와 일치하는 경우
      cards1.popleft()
      goal.popleft()
    elif cards2 and cards2[0] == goal[0]:  # ➌ card2의 front와 일치하는 경우
      cards2.popleft()
      goal.popleft()
    else:
      break  # 일치하는 원소를 찾지 못했으므로 종료

  return "Yes" if not goal else "No"  # ➍ goal이 비었으면 “Yes” 아니면 “No”를 반환
