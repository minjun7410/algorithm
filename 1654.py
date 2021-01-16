# 1. 가장 긴 랜선을 반 씩 자른다.
# 다른 것도 아닌 가장 긴 랜선인 이유 = 가장 많이 쪼갤 수 있는 랜선이기 때문이다.
# 2. 반 씩 잘라서 이분탐색으로 잘릴 수 있는 짧아서 못 자르는 랜선을 구분
# 3. (list) 못 자르는 랜선은 그대로 두고 잘릴 수 있는 랜선은 *2 처음 자를 수 있는 랜선은 1로 초기화
# 4. 그 다음 모두 더한 값이 K를 넘으면 break 후 가장 최근에 자른 랜선의 길이를 출력

# 위의 계획은 틀림 (반으로 쪼개는 걸로는 최대의 길이를 찾지 못함)

# 1. 길이가 1부터(start) 가장 큰 랜선의 길이(end) 로 이분탐색을 진행. ( 길이로 자를 때 랜선 수의 합)
# 2. 이분 탐색으로 K와 K+1의 경계를 찾는다.


# 이분탐색을 사용할 수 있는 폭이 큼을 알게 됨(지금까지 내가 했던 이분탐색은 1 2 4 6 7 에서 2를 찾는 것이였지만 이번 문제에서는 1 2 3 4 5 6 에서 4에 해당하는 랜선의 수를 구함)
# 굳이 리스트를 사용하지 않고 문제를 해결 할 수 있음


def binary_search(long_lan):
    start = 1
    end = long_lan
    while start <= end:
        mid = (start + end) // 2
        length = 0
        for i in origin_lan:
            length += i // mid

        if length >= K:
            start = mid + 1
        else:
            end = mid - 1
    return end


N, K = map(int, input().split())
origin_lan = [int(input()) for _ in range(N)]
long_lan = max(origin_lan)

result = binary_search(long_lan)

print(result)
    
