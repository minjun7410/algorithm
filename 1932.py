N = int(input())
value = [[] for _ in range(N)]

for n in range(N):
    value[n] = list(map(int, input().split()))

max_value = [[] for _ in range(N)]
max_value[0] = [value[0][0]]
for layer in range(1, N):
    for index in range(layer+1):
        if index - 1 < 0:
            right_max = max_value[layer-1][index] + value[layer][index]
            max_value[layer].append(right_max)
        elif index == layer:
            left_max = max_value[layer-1][index-1] + value[layer][index]
            max_value[layer].append(left_max)
        else:
            right_max = max_value[layer-1][index] + value[layer][index]
            left_max = max_value[layer-1][index-1] + value[layer][index]
            max_value[layer].append(right_max if right_max > left_max else left_max)


print(max(max_value[-1]))
