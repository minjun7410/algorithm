N = int(input())
lst = []
result = 1
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
lst.sort(key=lambda x: x[1])
tmp = lst[0]
for value in range(1, len(lst)):
    if lst[value][0] < tmp[1]:
        continue
    result += 1
    tmp = lst[value]
print(result)