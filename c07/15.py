"""
N에 대해서 반복 :
    (자기 넘버) + (K-1) 인 것 없앰.

    
만약 N = 5, K = 2

1 + 1 -> 2제거
3 + 1 -> 4제거
5 + 1 -> 1제거

queue로 구현.

append

while (q.qsize > 1)

"""

from collections import deque

def solution(N, K):
    queue = deque()

    for i in range(N):
        queue.append(i+1)
    
    while len(queue) > 1:
        for _ in range(K-1):
            queue.append(queue.popleft())

            queue.popleft()
    return queue[0]

print(solution(5, 2))
