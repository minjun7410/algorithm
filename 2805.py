#  1654와 같은 맥락의 문제
#  1부터 max(trees)까지 들고 갈 나무의 갯수를 이분탐색으로 찾는다.

#  경우의 수를 나열시키는게 이런 이분탐색으로 최댓, 최소값을 찾는 문제에서 해결 방안을 찾는 것에 도움이 되는 것 같다.
#  그러나 문제 분류를 보지 않고 최댓값을 찾는 이분탐색 문제가 나온다면 이런 방식으로 접근할 자신이 없다.

def binary_search(max_tree, M):
    start = 1
    end = max_tree - 1
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for value in trees:
            tmp += value - mid if value - mid > 0 else 0
        if tmp >= M:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2
    return end
            
N, M = map(int, input().split())
trees = list(map(int, input().split()))
max_tree = max(trees)  # 가장 긴 나무

end = binary_search(max_tree, M)
print(end)