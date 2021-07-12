# 플로이드 와샬 문제
# 자신이 몇번째인지 확인하는 방법은 아래 학생과 위 학생의 수를 합한게 N-1개인지 아닌지 확인하는것
# 그렇다면 해당 학생이 시작 정점일 때와 도착 정점일 때. INF가 아닌 갯수가 아래학생과 위학생을 합한것
# -> 플로이드 와샬

# 아직 플로이드 와샬의 메커니즘을 이해하지 못한듯.
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
table = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    start, end = map(int, input().split())
    table[start-1][end-1] = 1

for mid in range(N):  # mid : 거치는 정점
    for start in range(N): # start : 시작정점
        for end in range(N):
            if table[start][end] == 1: continue
            table[start][end] = 1 if table[start][mid] and table[mid][end] else 0
result = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            result[i] += 1
            result[j] += 1
print(result.count(N-1))