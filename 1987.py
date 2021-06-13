# dfs, bfs
# 처음 dfs로 풀었으나 계속된 시간초과로 bfs로 풀었더니 AC
# 가중치나 노드에 특징이 있으면 dfs로 써야한다고 생각했는데
# bfs로 푸니까 시간초과가 안났다.
# dfs로 풀었을 때 경로를 다시 돌아가는것 때문에 시간 초과가 생기는 것 같다.

import sys
input = sys.stdin.readline
from collections import deque

# input
R, C = map(int, input().split())
table = [list(map(str, input().rstrip())) for _ in range(R)]
# solution
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
alpha = {chr(char) : False for char in range(65, 91)}
alpha[table[0][0]] = True
def bfs():
    result = 0
    queue = deque([(0, 0, table[0][0])])
    while queue:
        y, x, sentence = queue.pop()
        result = max(result, len(sentence))
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx >= 0 and ny >= 0 and nx < C and ny < R and table[ny][nx] not in sentence:
                queue.append((ny, nx, sentence + table[ny][nx]))
    return result
def dfs(y, x, recursion):
    global result
    recursion += 1
    result = recursion if recursion > result else result
    for direction in range(4):
        nx = dx[direction] + x
        ny = dy[direction] + y
        if nx >= 0 and ny >= 0 and nx < C and ny < R and not(alpha[table[ny][nx]]):
            alpha[table[ny][nx]] = True
            dfs(ny, nx, recursion)
            alpha[table[ny][nx]] = False
    recursion -= 1
    return
result = bfs()
print(result)
