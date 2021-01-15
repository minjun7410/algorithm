N = int(input())
card = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
result = {}
'''def binary_search(target):
    start = 0
    end = len(card)-1
    mid = end // 2
    count = 0
    while end - start >= 0:
        if card[mid] > target:
            end = mid-1
            mid = (start + end) // 2
        elif card[mid] < target:
            start = mid+1
            mid = (start + end) // 2
        else:
            count += 1
            del card[mid]
            end -= 1
            mid = (start + end) // 2
            continue
    return count
'''
for target in card:
    if target in result:
        result[target] += 1
    else:
        result[target] = 1
for target in targets:
    if target not in result:
        print(0, end=' ')
        continue
    print(result[target], end=' ')
print()