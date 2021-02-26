# 다이나믹 프로그래밍 문제

# 상당히 점화식을 세우기 어려운 문제였었다. 
# 결국 검색해서 품
# 이 문제의 요점은 가로 블록이 2일 경우의 수가 3개인 것과 2n+2(n >= 1)일 경우의 수가 2이라는 것
# 즉 가로 길이가 4부터 4, 6, 8... 계속 경우의 수가 2개씩 쌓인다는 것

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
    dp[0] = 1  # 가로 길이가 2+2n일 때 성립되는 블록 조합 수 ( 4 : O 2+2 : X )
    dp[2] = 3  # 가로 길이가 2일 때 생각할 수 있는 블록 조합 수
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(0, i-3, 2):
            dp[i] += dp[j] * 2
    return dp[-1]


print(solution())
