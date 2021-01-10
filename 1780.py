import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
miners = 0
zero = 0
one = 0
def divide_conquer(y, x, size):
    global miners, zero, one
    count_m = 0
    count_z = 0
    count_o = 0
    for i in range(y, y+size):
        for j in range(x, x+size):
            if paper[i][j] == -1:
                count_m += 1
            elif paper[i][j] == 0:
                count_z += 1
            else:
                count_o += 1
    if count_m == size**2:
        miners += 1
        return
    elif count_z == size**2:
        zero += 1
        return
    elif count_o == size**2:
        one += 1
        return
    else:
        for i in range(3):
            for j in range(3):
                divide_conquer(y+i*size//3, x+j*size//3, size//3)
divide_conquer(0, 0, N)
print(miners)
print(zero)
print(one)