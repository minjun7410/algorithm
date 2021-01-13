MOD = 1000000007
def matrix_times(matrix_1, matrix_2):  #행렬끼리 곱셈
    mat_res = [[] for _ in range(len(matrix_1))]
    for i in range(len(matrix_1)):  # 가로
        for j in range(len(matrix_2)):  # 세로
            column = matrix_1[i]
            row = [matrix_2[n][j] for n in range(len(matrix_2))]
            result = [(x * y) % MOD for x, y in zip(column, row)]
            mat_res[i].append(sum(result) % MOD)
    return mat_res


N = int(input())

matrix = [[1, 1], [1, 0]]  #행렬으로 피보나치수 구하기. 행렬로 구하는 경우는 거듭제곱으로 구할 수 있기 때문에 O(logn) (google keep)
res = None
while N != 0:
    if N % 2 == 1:
        res = matrix_times(res, matrix) if res else matrix
    matrix = matrix_times(matrix, matrix)
    N //= 2
print(res[0][1])