result = []
lst = []

N = int(input())
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
for i in lst:
    ranking = 1
    for j in lst:
        if i == j: continue
        if i[0] < j[0] and i[1] < j[1]:
            ranking += 1
    result.append(ranking)
print(' '.join(map(str, result)))