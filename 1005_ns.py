# 그래프이론, 다이나믹 프로그래밍, 위상정렬
# 위상 정렬을 공부할 필요가 있을 것 같다. 그래프 이론, 다이나믹 프로그래밍으로 풀 방법이 생각이 안난다.

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # input
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    vertex = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        vertex[X].append(Y)
    W = int(input())
    # solution
    # ----------------s