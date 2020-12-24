N = int(input())
tiles = [0 for _ in range(N+1)]


def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif tiles[n]:
        return tiles[n]
    tmp = tile(n-1) + tile(n-2)
    tiles[n] = tmp
    return tmp


tile(N)
print(tiles[N] % 15746)
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