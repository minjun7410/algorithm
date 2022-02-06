
# BFS

# 1. 일단 부숴지는 미네랄 위치를 찾는다.
# 2. 미네랄을 부수고 상하좌우로 탐색을 한다.
# 3. 탐색할 때 클러스터 구성원(블럭)의 위치를 리스트에 저장하고 테이블에서 'x' 에서 '.'으로 바꾼다.
# 4. 탐색이 끝난 후 블럭들의 최소 땅 도는 다른 클러스터와의 거리를 반복문으로 구한다.
# 5. 모든 블럭을 최소 거리로 아래로 내린다.

from collections import deque

# 좌, 하, 우, 상
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

INF = 999999999

my, mx = map(int, input().split())
mineral_map = []
for _ in range(my):
    temp_list = [_ for _ in input()]
    mineral_map.append(temp_list)
input()

def BFS(target_x, target_y):
    result = [(target_x, target_y)]  # 해당 클러스터 미네랄의 위치 리스트
    visited_map = [[0 for _ in range(mx)] for _ in range(my)]  # 방문 표시를 위한 리스트
    visited_map[target_y][target_x] = 1
    queue = deque([(target_x, target_y)])
    mineral_map[target_y][target_x] = '.'
    while queue:  # 탐색을 통해 클러스터 미네랄의 위치를 result에 구하고 mineral_map에 '.'으로 갱신시킨다.
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or ny < 0 or nx >= mx or ny >= my: continue  # out of range
            if mineral_map[ny][nx] == '.' or visited_map[ny][nx] == 1: continue  # '.'이거나 이미 방문했으면 패스
            result.append((nx, ny))
            visited_map[ny][nx] = 1  # 방문처리
            queue.append((nx, ny))
            mineral_map[ny][nx] = '.'  # 테이블 갱신
    fall_number = -1
    flag = True
    while flag:  # 얼마나 떨어지는지 반복문을 통해 검사
        fall_number += 1
        for x, y in result:
            ny = y + fall_number
            if ny >= my or mineral_map[ny][x] == 'x':
                flag = False
                break
    for x, y in result:  # 테이블 갱신
        mineral_map[y+fall_number-1][x] = 'x'





for index, target_y in enumerate(list(map(int, input().split()))):
    target_y = my - target_y
    for target_x, value in enumerate(mineral_map[target_y]) if index % 2 == 0 else reversed(list(enumerate(mineral_map[target_y]))):  # 좌, 우 교대로 부술 y 위치를 구한다.
        if value == 'x':  # 부술 미네랄 위치를 찾음
            mineral_map[target_y][target_x] = '.'  # 부수기
            for dir in range(4):
                nx = target_x + dx[dir]
                ny = target_y + dy[dir]
                if nx < 0 or ny < 0 or nx >= mx or ny >= my: continue  # out of range
                if mineral_map[ny][nx] == '.': continue  # 이 위치에 미네랄이 없으면 패스
                BFS(nx, ny)
            break

for column in mineral_map:  # 프린트
    print(''.join(column))

