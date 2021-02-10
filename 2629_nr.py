# 동적계획법, 냅색 문제
# 주어진 추로 모든 무게의 가능성을 구해야한다.
# dp[i+1][j+weight[i]] = dp[i][w]
# dp[x][y] = True or False
N = int(input())
weight = list(map(int, input().split())) + [0]
dp = [[False for _ in range(15001)] for _ in range(N+1)] # 최악의 경우 추의 개수가 50이고 모든 추의 무게가 500인 경우 
def dynamic_recursion(i, j):
    if i > N or dp[i][j]:
        return
    dp[i][j] = True
    dynamic_recursion(i+1, j)
    dynamic_recursion(i+1, j + weight[i])
    dynamic_recursion(i+1, abs(j - weight[i]))
dynamic_recursion(0,0)
M = int(input())
result = []
for i in list(map(int, input().split())):
    if i > 15000:
        result.append('N')
        continue
    if dp[N][i]:
        result.append('Y')
    else:
        result.append('N')
print(' '.join(map(str, result)))

# 냅색 문제라는 정보를 얻고 너무 냅색에만 집중하니까 
# 재귀를 사용하는 것을 놓쳤음
# 단계별 풀어보기 라고 해도 푸는 방식을 자유롭게 할 필요가 있음