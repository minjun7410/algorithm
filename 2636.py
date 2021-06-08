# BFS 문제
# 덱은 현재 덱, 다음 덱 이렇게 구분한다.
# 현재 덱에는 0을 포함하고, 다음 덱은 녹을 치즈를 포함한다.
# 처음에는 가장자리 0을 다음 덱에 포함한다.
# 1. 현재 덱을 다음 덱으로 하드 카피한다.
# 2. 덱에 포함된 노드는 table을 0으로 바꾸고 상하좌우 노드들을 조사한다.
# (0이면 현재 덱에 포함, 1이면 다음 덱에 포함)
# 3. 현재 덱에 아무것도 안남을 떄 까지 1, 2를 반복

# 다음 덱에 아무것도 안남아 있을 때 1~3 반복을 종료한다.

import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# input
N, M = map(int, input().split())
table = [[2 for _ in range(M+2)] for _ in range(N+2)]
for i in range(1, N+1):
    seq = list(map(int, input().split()))
    for j in range(1, M+1):
        table[i][j] = seq[j-1]
# 가장자리 구하기
next = deque([(y, x) for y in range(0, N+2) for x in [0, M+1]] + [(y, x) for y in [0, N+1] for x in range(0, M+2)])
result = 0  # 녹은 시간
last = 0  # 마지막 남은 치즈 개수
while next:
    last = len(next)
    present = next  # 카피
    next = deque([])
    while present:
        y, x = present.popleft()
        for direction in range(4):
            ny = y + dy[direction]
            nx = x + dx[direction]
            if nx < 0 or nx > M+1 or ny < 0 or ny > N+1:    continue
            if table[ny][nx] == 0:
                table[ny][nx] = 2
                present.append((ny, nx))
            elif table[ny][nx] == 1:
                table[ny][nx] = 2
                next.append((ny, nx))
            else:
                continue
    result += 1
print(result-1)
print(last if result-1 != 0 else 0)  # 한번도 녹지 않았을 떈 last가 가장자리 개수가 되어버리므로