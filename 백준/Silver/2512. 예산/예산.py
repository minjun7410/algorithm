import sys
input = sys.stdin.readline
N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start = 0
end = max(budget)
mid = None
while start <= end :
    mid = (start+end) // 2
    num = 0
    for b in budget:
        if b > mid:
            num += mid
        else:
            num += b
    if num <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)