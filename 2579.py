N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
max_memory = [0 for _ in range(N)]
tmp = 0
for index, value in enumerate(stairs):
    if index == 0:
        max_memory[index] = value
        continue
    elif index == 1:
        max_memory[index] = value + max_memory[0]
        continue
    elif index == 2:
        one = value + stairs[index - 1]
        two = value + stairs[index - 2]
        max_memory[index] = one if one > two else two
        continue
    else:
        one = value + stairs[index - 1] + max_memory[index - 3]
        two = value + max_memory[index - 2]
        max_memory[index] = one if one > two else two
print(max_memory[-1])