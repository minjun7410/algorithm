# dfs
#

import sys
input = sys.stdin.readline

# input
R, C = map(int, input().split())
table = [list(map(str, input().rstrip())) for _ in range(R)]
result = 0
# solution
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
alpha = {chr(char) : False for char in range(65, 91)}
alpha[table[0][0]] = True

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
dfs(0, 0, 0)
print(result)
