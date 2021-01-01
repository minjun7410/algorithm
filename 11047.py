N, K = map(int, input().split())
lst = []
result = 0
for _ in range(N):
    lst.append(int(input()))
for value in lst[::-1]:
    while value <= K:
        result += 1
        K -= value
    if not(K):
        break
print(result)