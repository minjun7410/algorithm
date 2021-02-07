# 동적계획법 문제 
# my proposition
# i ~ j 의 펠린드롬 성립 여부 = dp[i][j]
# dp[i+1][j-1] == 1 and i == j (단 j - i > 1)

import sys
input = sys.stdin.readline
N = int(input())
board = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
def dynamic_programming():
    for length in range(1, N+1):
        for i in range(1, N-length+2):  # i: 시작위치 j: 종료위치
            j = i + length - 1
            if length == 1:
                dp[i][i] = 1
            elif length == 2 and board[i] == board[j]:
                dp[i][j] = 1
            elif dp[i+1][j-1] == 1 and board[i] == board[j]:
                dp[i][j] = 1
dynamic_programming()
for _ in range(int(input())):
    start, end = map(int, input().split())
    print(dp[start][end])