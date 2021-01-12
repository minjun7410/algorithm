MOD = 1000

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix = [list(map(lambda x: x % MOD, lst)) for lst in matrix]
def matrix_time(mat_1, mat_2):
    temp_mat = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N):  # mat_1의 가로
        for j in range(N):  # mat_2 의 세로
            column = mat_1[i]
            row = [mat_2[x][j] for x in range(N)]
            tmp = sum([n * m for n, m in zip(column, row)])
            temp_mat[i][j] = tmp % MOD
    return temp_mat

sums = None
while B > 0:
    if B % 2 == 1:
        sums = matrix_time(sums, matrix) if sums else matrix
    matrix = matrix_time(matrix, matrix)
    B //= 2

for lst in sums:
    print(' '.join(map(str, lst)))

