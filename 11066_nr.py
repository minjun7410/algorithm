# 동적계획법 문제
# 점화식 세우는 것을 연습
# j = start index   i = sequence length
# dp[x][x+y] = x부터 y까지 파일 크기 합
# dp[i][j] = dp[i][k] + dp[k+1][j] + sum(i~j)

#이후 knuth algorithm을 이용하여 문제를 풀어야겠다.
#O(n^3) -> O(n^2)


MAX = 999999999
for _ in range(int(input())):
    N = int(input())
    chapter = []
    chap_sum = [0 for _ in range(N)]
    for index, value in enumerate(map(int, input().split())):
        chapter.append(value)
        if index == 0:
            chap_sum[0] = value
        else:
            chap_sum[index] = chap_sum[index-1] + value
    chapter = [0] + chapter
    chap_sum = [0] + chap_sum
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for i in range(1, len(chapter)): # i는 구간의 길이
        for j in range(1, N-i+1): # j는 시작점
            dp[j][j+i] = MAX
            for k in range(j, i+j): # k는 구간에서 2구간으로 나누는 위치
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + (chap_sum[j+i] - chap_sum[j-1]))
    result = 0
    for i in range(N+1):
        result = max(result, dp[i][-1])
    print(result)

