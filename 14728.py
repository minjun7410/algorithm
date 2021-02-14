# 여러 단원과 배점이 주어지고 최고의 가치를 가지는 조합 찾기 -> 냅색일 가능성
import sys
input = sys.stdin.readline
# input
N, T = map(int, input().split())
K = [0]
S = [0]
for _ in range(N):
    k, s = map(int, input().split())
    K.append(k)
    S.append(s)
# answer
dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, T+1):
        if j - K[i] < 0:
            dp[i][j] = dp[i-1][j] # <--
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-K[i]]+S[i])
print(dp[-1][-1])

# ymjoo12 
#이차원 배열로 매번마다 새로운 배열을 채울 경우에는 dp[i][k:t+1] 구간만 업데이트하면, 

#dp[i][:k] 구간은 채워지지 않기 때문에 (dp[i-1][:k] 로 채워줘야 하는데 0인 상태로 남아있기 때문에)

#잘못된 값이 나올 수 밖에 없습니다.

#따라서 코드에서 처럼 이차원 배열을 이용하는 경우에는 dp[i][:] 전체에 값을 채워주면서 

#t < k일 경우에는 dp[i][j] = dp[i-1][j] 로 채워주는 조건문을 추가해야합니다.