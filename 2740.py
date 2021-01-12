N, M = map(int, input().split())
matrix_A = []
for _ in range(N):
    matrix_A.append(list(map(int, input().split())))

M, K = map(int, input().split())
matrix_B = [[] for _ in range(K)]
for i in range(M):
    for index, j in enumerate(map(int, input().split())):
        matrix_B[index].append(j)

for i in range(N):
    for j in range(K):
        result = [x * y for x, y in zip(matrix_A[i], matrix_B[j])]
        print(sum(result), end=' ')
    print()
