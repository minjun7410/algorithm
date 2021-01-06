'''def pascal(N, M): # 이항계수를 이용하는 문제인줄 알았으나 의상 각각의 갯수가 있으므로 불가능.
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, N+1):
        dp[i][0] = 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i][i] = 1
    return dp[N][M]'''


T = int(input())

for _ in range(T):
    n = int(input())
    costume = {}
    for _ in range(n):
        a, b = input().split()
        if b in costume:
            costume[b] += 1
        else:
            costume[b] = 1
    result = 1
    for value in costume.keys():
        result *= costume[value]+1  # 의상의 종류가 3이라면 투명 의상을 생각해서 종류가 4가 됨, 각각 의상의 종류 갯수를 곱하고 -1(맨몸의 경우 제외)을 함. (안입는 경우를 생각해서 하나씩 입는 경우, 두개씩 입는 경우들을 해결함.)
    print(result-1)