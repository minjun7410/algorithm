# 1300 chogahui05
# 1 2 3
# 2 4 6
# 3 6 9
# 1부터 9까지의 범위를 이분 탐색한다.
# ex) 처음 5가 타깃일 때 min(N, 5//1) + min(N, 5//2) + min(N, 5//3) 으로 5이하 갯수를 구하고 (N의 제곱을 모두 연산할 필요없고 1부터 N까지 나눗셈으로 N번의 연산할 수 있다.)
# K와 비교해서 다음 탐색을 진행한다.
N = int(input())
K = int(input())


def binary_search(K):
    start = 1
    end = N ** 2
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(1, N+1):
            count += min(N, mid // i)
        if count >= K:
            end = mid - 1
        else:
            start = mid + 1
    return start  # 배열 A와 B의 인덱스는 1부터 시작함.

print(binary_search(K))