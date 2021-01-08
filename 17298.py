N = int(input())
lst = list(map(int, input().split()))
result = [-1 for _ in range(N)]
yet = []
for i in range(N):
    for j in range(len(yet)-1, -1, -1):
        if lst[i] > yet[j][1]:
            index, value = yet.pop()
            result[index] = lst[i]
        else:
            break
    yet.append((i, lst[i]))  # (index, value)
print(' '.join(map(str, result)))