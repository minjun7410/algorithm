# 다이나믹 프로그래밍 문제

import sys
input = sys.stdin.readline

# input
N = int(input())

# answer


def solution():
    if N % 2 != 0:
        return 0
    elif N < 4:
        return 3
    dp = [0 for _ in range(N+1)]
    dp[0] = 1  # 가로 길이가 4일 때 성립되는 블록 조합 수 ( 4 : O 2+2 : X )
    dp[2] = 3  # 가로 길이가 2일 때 생각할 수 있는 블록 조합 수
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3 + dp[i-4] * 2
    print(dp)
    return dp[-1]


print(solution())
