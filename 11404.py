# 플로이드 와샬 알고리즘
# 하나의 정점에서 모든 정점까지 거리를 계산하는게 아닌
# 모든 정점에서 모든 정점의 거리 (단 음수는 없음. 음수가 있다면 벨만 포드)를 모두 조사해야하므로
# -> 플로이드 와샬 알고리즘

# 플로이드 와샬 알고리즘은 "거쳐가는 정점"를 기준으로 최단거리를 구한다
# https://blog.naver.com/ndb796/221234427842

import sys
input = sys.stdin.readline
INF = 87654321


# input
n = int(input())
matro = [[INF for _ in range(n)] for _ in range(n)]
for i in range(0, n):
    matro[i][i] = 0
for _ in range(int(input())):
    start, end, distance = map(int, input().split())
    matro[start-1][end-1] = min(matro[start-1][end-1], distance)

# solution
for node in range(0, n):  # node : 거쳐가는 정점
    for start in range(0, n):  # start : 시작 정점
        for end in range(0, n):  # end : 도착 정점
            # if start == end or start == node or end == node:  continue
            # 거쳐가는 정점이 시작 정점이거나 도착 정점이면 조사할 필요가 없으므로 위 구문을 사용했지만 시간이 더 걸린다.
            tmp = matro[start][node] + matro[node][end]
            matro[start][end] = min(matro[start][end], tmp)

for i in range(0, n):
    print(" ".join(map(str, map(lambda x: 0 if x == INF else x, matro[i]))))