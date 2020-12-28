#  두 줄이 합선 되는 지 검사하는 함수 필요
#  1부터 N까지 순서대로 검사하고 각각 최대값 구하기(예: 1-1 2-3 3-2 4-4 에서 4를 검사하면 2-3, 3-2의 최대값은 1이고 그 둘은 4-4와 합선되지 않으므로 2-3의 최대값 + 1이 4-4의 최대값이다.)


def is_cross(a, b):  # 교차하는지 검사
    if (a[0] - b[0])*(a[1] - b[1]) < 0:
        return True
    else:
        return False


N = int(input())
power_pole = []
dp = [1 for _ in range(N)]

for _ in range(N):
    power_pole.append(tuple(map(int, input().split())))
    
power_pole.sort(key = lambda x: x[0])

for index in range(N):
    for negative in range(1, index + 1):
        target_index = index - negative
        if not(is_cross(power_pole[index], power_pole[target_index])):
            dp[index] = max(dp[index], dp[target_index] + 1)

print(N-max(dp))

    