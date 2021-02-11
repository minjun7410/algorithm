# 동적계획법, 냅색 문제
# 가장 비용이 적은 조합을 찾아야함, -> 냅색 문제로 생각 가능
# dp[i][j] = max(dp[i-1][j], byte[i] + dp[i-1][j-cost[i]])
# if weight[i] + dp[i-1][j-i] > M
# min_value = min(min_value, j)
N, M = map(int, input().split())
byte = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(N*max(cost)+1)] for _ in range(N+1)]
result = 12345678
for i in range(1, N+1):
    for j in range(N*max(cost)+1):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], byte[i] + dp[i-1][j-cost[i]])
        if dp[i][j] >= M:
            result = min(result, j)
print(result)

# byte를 j로 하기에는 크기가 너무 커질 수 있기 때문에 cost를 j로 하고 매번 비용 검사를 거쳐서 최소의 비용을 구했다.
# 중요한 것은 j는 비용이지만 다른 냅색 문제와는 다르게 dp[i][j] 는 비용이 아닌 byte라는 점
'''
i/j	  0	 1	2	3	4	5	6	7	

0(0)  0	 0	0	0	0	0	0	0							 

1(30) 0	 0	0	30	30	30	30	30						

2(10) 10 10 10	10	30	40	40	40		

3(20) 10 10	10	10	30	40	50	60											

3(35)	...

4(40)  ...
'''