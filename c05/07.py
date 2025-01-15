"""
#내 풀이
def solution(dirs):
    visited = [[False for _ in range(5)] for _ in range(5)]
    x = 0
    y = 0

    for i in range(len(dirs)):
        count = 0
        if (dirs[i] == 'U'):
            y +=1
        elif (dirs[i] == 'D'):
            y -= 1
        elif (dirs[i] == 'R'):
            x += 1
        else:
            x -= 1
        if (not visited[x][y]) and (-5 <= x <= 5) and (-5 <= y <= 5):
            visited[x][y] == True
            count +=1
    return count

"""

#고친 풀이
def solution(dirs):
    visited = set()  # 방문한 길을 저장할 집합
    x, y = 0, 0  # 시작 좌표 (0, 0)

    # 방향에 따른 이동 변화량
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for direction in dirs:
        nx, ny = x + moves[direction][0], y + moves[direction][1]

        # 범위를 벗어나면 무시
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 양방향으로 길을 저장
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))

            # 현재 위치 갱신
            x, y = nx, ny

    return len(visited) // 2  # 길은 양방향으로 저장되므로 절반을 반환

#저자 풀이
def is_valid_move(nx, ny) : # ➊ 좌표를 벗어나는지 체크하는 함수
  return 0 <= nx < 11 and 0 <= ny < 11
 
def update_location(x, y, dir) : # ➋ 명령어를 통해 다음 좌표를 결정
  if dir == 'U':
    nx, ny = x, y + 1
  elif dir == 'D':
    nx, ny = x, y - 1
  elif dir == 'L':
    nx, ny = x - 1, y
  elif dir == 'R':
    nx, ny = x + 1, y
  return nx, ny

def solution(dirs):
  x, y = 5, 5
  ans = set( ) # ➌ 겹치는 좌표는 1개로 처리하기 위함
  for dir in dirs : # ➍ 주어진 명령어로 움직이면서 좌표 저장
    nx, ny = update_location(x, y, dir)
    if not is_valid_move(nx, ny) : # ➎ 벗어난 좌표는 인정하지 않음
      continue
    # ➏ A에서 B로 간 경우 B에서 A도 추가해야 함(총 경로의 개수는 방향성이 없음)
    ans.add((x, y, nx, ny))
    ans.add((nx, ny, x, y))
    x, y = nx, ny # ➐ 좌표를 이동했으므로 업데이트
  return len(ans)/2

"""
note : 
- 좌표가 범위를 벗어나면 무시해야 하므로, 범위를 벗어나기 전에 U, D, R, L 등의 좌표 계산 처리를 하지 말아야 한다.
- 따라서 명령어에 따라 이동할 좌표를 미리 계산한 후, 해당 좌표가 범위 내에 있을 때만 visited에 이동을 해서 "이동했음"을 체크
- 내 풀이는 범위를 체크하기 전에 미리 좌표 계산 처리를 했고, 그 다음에 도착한 점에만 visited = True를 지정을 했고, 조건을 만족시키면 length를 1 증가시킴. 엉터리 코드
- 그리고 미리 모든 좌표에 대한 visited 배열을 만들지 않아도 된다. 그냥 갈수 있으면 이동하고, 이동한 경로를 visited에 저장을 하고,
- (경로이므로 진짜 경로 길이보다 2배로 visited에 저장이 됨) 나중에 len(visited)를 2로 나눠 반환하면 된다.
- 나는 visited 배열을 순전히 이동했다고 True가 나오면 이동 못하게 하는 방식으로 썼다. 하지만 visited에 담기면 이동했다는 뜻이므로, 그리고 여기서 모든 길이는 1이므로,
- visited 배열의 길이가 곧 내가 간 path의 길이가 된다. ***최대한 넓게 사고하기!!!!
"""
