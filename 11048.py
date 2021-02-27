# 다이나믹 프로그래밍 문제
# 언뜻 보면 BFS 문제처럼 보이고 BFS로 풀 수 있을 것 같다.
# 하지만 문제의 조건은 오른쪽 또는 아래 밖에 못 움직인다.
# 이는 각 방마다 몇번째 이동으로 그 방으로 갈 수 있는지 정해져있다는 뜻임

# 따로 NXM 배열을 만든다. (이것은 dp를 저장하는 배열)
# 이중포문으로 모든 방을 검사하는데
# 이때 오른쪽 or 아래쪽 포지션 방과 현재 방(dp)의 합이 그 방(dp)보다 크면 갱신한다.
import sys

# input
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# answer
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = table[0][0]
for i in range(N):
    for j in range(M):
        if i + 1 < N:
            tmp = dp[i][j] + table[i+1][j]
            dp[i+1][j] = max(dp[i+1][j], tmp)
        if j + 1 < M:
            tmp = dp[i][j] + table[i][j+1]
            dp[i][j+1] = max(dp[i][j+1], tmp)
print(dp[-1][-1])

