N = int(input())
tiles = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        tiles[i] = 1
    elif i == 2:
        tiles[i] = 2
    else:
        tiles[i] = (tiles[i-1] + tiles[i-2]) % 15746

print(tiles[N])
'''
def tile_01(n):
    if tiles[n]:
        return tiles[n]
    if n == 2:
        return ["00", "11"]
    if n == 1:
        return ["1"]
    for tmp in tile_01(n-1):
        for i in ['0', '1']:
            left = i + tmp
            right = tmp + i
            if is_possible(left):  # 0이 이어서 홀수개면 False
                tiles[n].append(left)
            if tmp[0] == tmp[-1]:  # '00', '11'인 경우를 대비
                continue
            if is_possible(right):
                tiles[n].append(right)
    return tiles[n]


def is_possible(tile):
    sums = 0
    for char in tile:
        if char == '1' and sums % 2 == 1:
            return False
        elif char == '1' and sums % 2 == 0:
            break
        else:
            sums += 1
    for char in tile[::-1]:
        if char == '1' and sums % 2 == 1:
            return False
        elif char == '1' and sums % 2 == 0:
            return True
        else:
            sums += 1

    return True


tile_01(N)

print(len(tiles[N]) % 15746)'''