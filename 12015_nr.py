# 1. 증가하는 수열을 저장하는 리스트 만든다. [0]
# 2. 리스트 꼬리와 입력받은 수를 비교해서
# 꼬리보다 크면
# append
# 꼬리보다 작으면
# 입력받은 수와 같거나 큰 수 중 가장 가까운 수를 입력받은 수와 교체한다.
# 3. 반복문이 끝나면 리스트 - 1 이 가장 긴 증가하는 부분 수열의 길이이다.(처음 초기값 0을 넣어주었기 때문)


def binary_search(value):
    start = 0
    end = len(result) - 1
    while start <= end:
        mid = (start + end) // 2
        if result[mid] >= value:
            end = mid - 1
        else:
            start = mid + 1
    return start


result = [0]
N = int(input())
lst = list(map(int, input().split()))
for value in lst:
    if value > result[-1]:
        result.append(value)
    elif value < result[-1]:
        result[binary_search(value)] = value
    print(result)
print(len(result) - 1)

# 최종 리스트 전체를 구하는 문제가 아니라 최대 개수를 구하는 문제이므로 마지막에 남는 리스트를 상관하지 않아도 됨
# 최대 연속하는 리스트 x, 그 다음으로 최대 연속하는 리스트 y라고 하면
# (x > y)
# A = [x1, x2, x3, y1, y2] 일때
# result = [y1, y2, x3]
# 따라서 답은 리스트 x의 길이가 된다.